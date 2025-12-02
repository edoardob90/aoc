#!/usr/bin/env wolframscript
(* ::Package:: *)

int = Interpreter["Integer"];

{ts, busIDs} = MapAt[
   StringCases[t:DigitCharacter..~~","|EndOfLine:>int@t], StringSplit@$ScriptInputString, 2]


(* ::Section:: *)
(*Part 1*)

(* ::Text:: *)
(*A function to find the divisors of a number n within the range [n, n+\[Delta]]*)

divisorsAround[n_,\[Delta]_,div_]:=
<|div-> Select[Range[n,n+\[Delta]],Divisible[#,div]&]-n|>


(* ::Text:: *)
(*As delta we use the largest bus ID which is the largest period of time after which that bus will start a new ride*)

divs = divisorsAround[int@ts, Max@busIDs, #]&/@ busIDs//Apply@Join//Map@Min//Sort

Print[
 StringTemplate["--- Part 1 ---\nID of the earliest bus multiplied by the number of waiting minutes: ``"][First@KeyValueMap[#1*#2&, divs]]
 ]


(* ::Section:: *)
(*Part 2*)

(* ::Text:: *)
(*This is an example of a "Chinese remainder problem", that is, finding the smallest positive integer x that satisfies simultaneously a series of remainder congruences.*)
(**)
(*Suppose that a bus with id "K" appears in the position "i" in the list. That means that bus K should depart at time "t + i", and this implies that Mod[t+i, K] == 0. This must be valid for all the buses in the list, and the smallest t>=0 that satisfies all these equalities is our "timestamp".*)

(* ::Text:: *)
(*First, we write a small function that builds an association of <| K -> i |> for all K and i.*)

getBusOffsets[s_]:=
 With[{IDs = int/@StringSplit[s//StringSplit//Last//StringReplace["x"->"0"],","]},
Association@@Cases[IDs,n_/;n!=0:>n-> First@Flatten@Position[IDs,n]-1]
]

busOffsets = getBusOffsets[$ScriptInputString];

ts = FindInstance[KeyValueMap[Mod[t+#2,#1]==0&, busOffsets], t, Integers]
Print[
StringTemplate["\n--- Part 2 ---\nEarliest timestamp: ``"][t/.First@ts]
]

(* ::Text:: *)
(*Or, a more compact and somewhat elegant solution is*)

(*ChineseRemainder@@{-Values@busOffsets, Keys@busOffsets}*)
