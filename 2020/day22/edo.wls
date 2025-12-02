#!/usr/bin/env wolframscript
(* ::Package:: *)

int = Interpreter["Integer"];
cards = StringSplit[
  $ScriptInputString,"\n\n"] // 
   StringCases[DigitCharacter..]//Map[Rest/*int];


(* ::Section:: *)
(*Part 1*)

ClearAll[play];
play[cards_List]:=
  Block[{p1=cards[[1]], p2=cards[[2]]},
   With[{c1=p1[[1]], c2=p2[[1]]},
    If[c1>c2,
    {Join[p1,{c1,c2}], p2},
    {p1, Join[p2,{c2,c1}]}
   ] // Map[Delete[1]]
  ]
]

score = With[
  {res=Join@@NestWhile[play, cards, Times@@Length/@#!=0&]},
  res.Reverse@Range@Length@res];
Print[StringTemplate["Final score = ``"][score]]


(* ::Section:: *)
(*Part 2*)

(* ::Text:: *)
(*Once again, a recursive problem. Things that we have to pay attention to:*)

(* ::ItemNumbered:: *)
(*The "infinite game prevention rule": player 1 wins if a round presents two decks of cards that we already encountered before*)

(* ::ItemNumbered:: *)
(*When recursing into sub-games, we have to keep track of which player is the winner. When coming back to the main game, we don't care about the winning cards, only who won*)

(* ::ItemNumbered:: *)
(*We use a "HashSet" data structure to keep track of already seen decks. Seems more efficient that appending to a simple list*)

ClearAll[playRecursive];
playRecursive[cards_List] :=
 Module[{d1, d2, decks = cards, c1, c2, 
   seen = CreateDataStructure["HashSet"], winner = 0, round = 0},
  While[winner == 0,
   Which[
    Length[decks[[2]]] == 0 || seen["MemberQ", decks], winner = 1,
    Length[decks[[1]]] == 0, winner = 2,
    True,
    (*Print[StringTemplate["Round n. ``"][++round]];*)
    seen["Insert", decks];
    {{c1, d1}, {c2, d2}} = 
     MapAt[First, TakeDrop[#, 1], 1] & /@ decks;
    
    (*Print[Column[{{c1, d1}, {c2, d2}}]];*)
    
    (* check if we need to run a sub-game *)
    If[Length@d1 >= c1 && Length@d2 >= c2,
     (* recurse into sub-game *)
     (*Print["New sub-game ..."];*)
     {decks, winner} = 
      playRecursive[Take[#2, UpTo@#1] & @@@ {{c1, d1}, {c2, d2}}];
     ];
     
    (* update cards *) 
    decks = If[winner == 1 || winner == 0 && c1 > c2,
      {Join[d1, {c1, c2}], d2},
      {d1, Join[d2, {c2, c1}]}
      ];
    winner = 0
    (*Print[Column[{decks}]];*)
    ]
   ];
  {decks, winner}
  ]

endgame = playRecursive[cards];
Print[
  StringTemplate["Final score of Recursive game = ``"][endgame[[1,2]].Reverse@Range@Length[endgame[[1,2]]]]
]
