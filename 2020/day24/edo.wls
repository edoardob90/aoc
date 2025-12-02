#!/usr/bin/env wolframscript
(* ::Package:: *)

(* ::Section:: *)
(*Part 1*)

moves = Alternatives @@ {"nw", "ne", "se", "sw", "e", "w"};

(* ::Text:: *)
(*This is taken from https://www.redblobgames.com/grids/hexagons/#coordinates where we are considering the parallelism between a 3D cube coordinates and a 3-axis hexagonal tiling*)

hexmoves = Thread[{"e", "ne", "nw", "w", "sw", "se"} -> 
   {{1, -1, 0}, (* e *)
    {1, 0, -1}, (* ne *)
    {0, 1, -1},(* 
    nw *)
    {-1, 1, 0}, (* w *)
    {-1, 0, 1}, (* 
    sw *)
    {0, -1, 1} (* se *)
    }]

tilesList = StringTrim /@ StringSplit[$ScriptInputString, "\n"];
Print[StringTemplate["Black tiles count = ``"][
Fold[Plus, #] & /@ StringCases[tilesList, moves] /. hexmoves // 
   Tally // Count[{_, _?OddQ}]
   ]
]

(* ::Section:: *)
(*Part 2*)

(* ::Text::Italic:: *)
(*Coming soon... Merry Coding Christmas, meanwhile ;-)*)
