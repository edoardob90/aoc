#!/usr/bin/env wolframscript
(* ::Package:: *)

int = Interpreter["Integer"];
numbers = int/@StringSplit["20,9,11,0,1,2", ","];

(* ::Text:: *)
(*There are to many Association operations that take too long. I don't know how I could improve it. There's only Part 1 here :-( *)

g[a_Association]:=
Block[{turn=Length@a+1,next,counts, posIdx,last},
  last=Last@Values@a;
  counts=Counts@*Values@a;
  next=If[counts[last]==1,0,
    posIdx=PositionIndex@a;
    Subtract@@Take[Reverse@posIdx[last],2]
   ];
   Append[a,<|turn->next|>]
]

With[{l=AssociationThread[Range@Length@numbers, numbers]},
  res=Nest[g, l, 2020-6]//Last//AbsoluteTiming;
  Print[res]
]

(* ::Text:: *)
(*This takes ~1.5 s so it's definitely too slow for the second part*)
