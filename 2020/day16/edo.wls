#!/usr/bin/env wolframscript
(* ::Package:: *)

(* ::Section:: *)
(*Part 1*)

{fields, my, nearby} = StringSplit[$ScriptInputString, "\n\n"];

(* ::Text:: *)
(*Build the union of all the intervals*)

fieldsLimits = IntervalUnion@@Interval/@StringCases[fields, i1:DigitCharacter..~~"-"~~i2:DigitCharacter..:> FromDigits/@{i1,i2}]

(* ::Text:: *)
(*The list of fields of nearby tickets*)

nearbyFields=Rest@StringSplit[nearby, "\n"]//Map[StringSplit[#,","]&]//Flatten//Map@FromDigits

(* ::Text:: *)
(*Check how many fields are invalid for any field*)

{r,{res}} = 
  Reap[
   Scan[If[!IntervalMemberQ[fieldsLimits,#], Sow[#]]&, Flatten@nearbyFields]
   ];
Print[StringTemplate["--- Part 1 ---\nTotal scanning error: ``"][Total@res]]
