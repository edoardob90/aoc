#!/usr/local/bin/wolframscript
(* ::Package:: *)

(* ::Section:: *)
(*Part 1*)

(*input = Import[$ScriptInputString, "List"];

(* Takes ~ 17 ms *)
Print[
With[{l = Union[Permutations[input, {2}]]},
  Times @@@ l[[Position[Total /@ l, 2020][[1]]]]
  ]
]*)

(* ::Text:: *)
(*The fastest is a pattern-matching approach*)

Print[
FromDigits /@ 
StringSplit[$ScriptInputString, "\n"] /. 
  {___,x_,___,y_,___} /; x+y == 2020 :> x y
]

(* ::Section:: *)
(*Part 2*)

(*(* Takes ~ 4 s *)
Print[
With[{l = Union[Permutations[input, {3}]]},
  Times @@@ l[[Position[Total /@ l, 2020][[1]]]]
  ]
]*)

Print[FromDigits /@ 
 StringSplit[$ScriptInputString, "\n"] /. 
   {___,x_,___,y_,___,z_,___} /; x+y+z==2020 :> x y z
]
