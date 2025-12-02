#!/usr/bin/env wolframscript
(* ::Package:: *)

foods = Flatten[
With[{input=StringSplit[$ScriptInputString, "\n"]},
StringCases[input,ing__~~" (contains "~~all__~~")" :> Union/@{StringSplit@ing, StringTrim/@StringSplit[all,","]}]
],1];

(* ::Section:: *)
(*Part 1*)

(* ::Text:: *)
(*First, build the lists of unique ingredients and allergens*)

allIngredients = Union@@foods[[All, 1]];
allAllergens = Union@@foods[[All, 2]];

(* ::Text:: *)
(*Count how many times each ingredients appears in the full list*)

ingredientCounts=Counts@Flatten@foods[[All, 1]];

(* ::Text:: *)
(*Any ingredient could potentially contain any allergen*)

couldBe = AssociationThread[allIngredients,
    Association@@Outer[Rule, allAllergens, {True}]
];

(* ::Text:: *)
(*We scan the list of food and, for each allergen, we remove the ingredients that for sure cannot contain it. The text says that if the allergen is listen, then the ingredient containing it must be in the ingredient list.*)
(*As usual, "Scan" is much faster than "Map".*)

Scan[
 Function[food,
  With[{allergens = Flatten@Outer[Rule, food[[2]], {False}],
   not = Complement[allIngredients, food[[1]]]},
    Scan[AssociateTo[couldBe[#], allergens]&, not]
  ]], foods];

(* ::Text:: *)
(*Now we select those ingredients that cannot contain any allergen: these are the elements of "couldBe" association whose values are all False.*)
(*We then take the counts of those ingredients and sum them up. That's Part 1's answer.*)

withoutAllegerns = 
 Keys@Select[couldBe, ContainsNone[Values@#, {True}] &];

p1 = KeyTake[ingredientCounts, withoutAllegerns] // Total;
Print[p1]

(* ::Section:: *)
(*Part 2*)

(* ::Text:: *)
(*This will be a recursive elimination.*)

(* ::Text:: *)
(*First, get those ingredients that must contain at least one allergen (eventually, an allergen can be present in at most one ingredient).*)

withAllergens = KeyDrop[couldBe, withoutAllegerns];

(* ::Text:: *)
(*The function below does three things:*)

(* ::ItemNumbered:: *)
(*Takes the ingredient with only one allergen: it's done for that ingredient since there's no other choice*)

(* ::ItemNumbered:: *)
(*Saves the above ingredient -> allergen in the final association*)

(* ::ItemNumbered:: *)
(*Delete any of the above allergens from all the remaining ingredients lists, and return that association*)

ClearAll[pruneIngredients];
pruneIngredients[I_Association] :=
 With[{sure = Select[I, Length@# == 1 &]},
  Module[{k, v},
   {k, v} = Through[{Keys, Flatten@*Values}[sure]];
   AssociateTo[canonical, AssociationThread[k, v]];
   DeleteCases[Alternatives @@ v] /@ 
    KeyTake[I, Complement[Keys@I, k]]
   ]
  ]

(* ::Text:: *)
(*We build an association of ingredients and their only possible candidates as allergens.*)

remaining = Select[TrueQ] /@ withAllergens // SortBy[Length] // Map[Keys];

(* ::Text:: *)
(*The final list begins as empty. Next, prune the ingredients lists until the result is an empty association: that means that each allergens have been assigned to one ingredient.*)

canonical = <||>;
FixedPoint[pruneIngredients, remaining];
p2 = StringRiffle[Keys@Sort@canonical, ","];
Print[p2]
