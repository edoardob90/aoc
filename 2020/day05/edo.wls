#!/usr/bin/env wolframscript
(* ::Package:: *)

(* Max number of rows and columns *)
{rows, cols} = {Range[0, 127], Range[0, 7]};


bisectList[list_, keep_] :=
 With[{p = Partition[list, Floor[Length@list/2]]},
  Which[
   StringMatchQ[keep, "F" | "L"], First@p,
   StringMatchQ[keep, "B" | "R"], Last@p
   ]
  ]


seats = StringSplit[$ScriptInputString,"\n"] //
           Map[TakeDrop[# // Characters,7]&];


seatIDs = First@Fold[bisectList,rows,First@#]8 + 
			First@Fold[bisectList,cols,Last@#]&/@seats//Sort;


Print["--- Part 1 ---\nHighest seat ID is "~~ToString@*Max@@seatIDs]


Print["--- Part 2 ---\nYour seat ID is "~~ToString@
        (Complement[Range[Min@@#,Max@@#],#]&/*First@seatIDs)]
