#!/usr/bin/env wolframscript
(* ::Package:: *)

(* ::Section:: *)
(*Part 1*)

(* ::Text:: *)
(*Function to modify a value given the mask*)

modifyValue[value_Integer,mask_String]:=
Block[{m=StringReverse/*Characters@mask, newvalue=0},
MapIndexed[
Switch[#1,
"X",newvalue+=BitAnd[value,2^(First@#2-1)],
"1",newvalue+=2^(First@#2-1),
_,Null
]&,m];
newvalue
]

(* ::Text:: *)
(*Use "Scan" instead of "Map" as in this case it's much faster*)

mem=<||>; (* empty association to collect new values *)

With[
{sample=StringSplit[$ScriptInputString,"mask"]//Map@StringTrim//Map[StringSplit[#,"\n"]&]//Map[MapAt[StringDelete["="|Whitespace],#,1]&]},
Scan[
First@*
  StringCases["["~~idx:DigitCharacter..~~"]"~~" = "~~val:DigitCharacter.. :> AssociateTo[mem,idx->modifyValue[int[val],#[[1]]]]]/@#[[2;;]]&, sample]]

Print[ToString[Total@mem]]
