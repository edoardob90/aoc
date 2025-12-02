#!/usr/bin/env wolframscript
(* ::Package:: *)

(* Traverse the map given as input with (right, down) jumps *)
computePath[input_][{right_:3,down_:1}]:=
Block[{nr,nc},
{nr,nc}=Dimensions@input;
 NestWhileList[
 {#[[1]]+Min[nr-#[[1]], down], Mod[#[[2]]+right,nc,1]}&, {1,1}, #[[1]] < nr&]
]

(* Count how many # *)
countHashtags[input_][path_]:=
input[[Sequence@@#]]&/@path//Count["#"]


input = $ScriptInputString//StringSplit//Map[Characters@#&];

Print["Part 1"]
path=computePath[input][{}];
Print["We crossed "~~ToString[countHashtags[input][path]]~~" trees"]


Print["Part 2"]
jumps = {{1,1},{3,1},{5,1},{7,1},{1,2}};
paths = computePath[input]/@jumps;
trees = countHashtags[input]/@paths;

Print["We would cross a total of "~~ToString[Times@@trees]~~" trees"]
