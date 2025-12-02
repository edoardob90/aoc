#!/usr/bin/env wolframscript
(* ::Package:: *)

int = Interpreter["Integer"];


fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"};
reqs = AssociationThread[fields, Join[Table[True, 7], {False}]];


passports = 
With[{pArr=Map[StringSplit[#,{WhitespaceCharacter,"\n"}]&, 
       StringTrim/@StringSplit[$ScriptInputString, StartOfLine~~EndOfLine]]},
Function[{p},
    StringSplit[#,":"]&/@p//Transpose//Apply[AssociationThread]//KeySort
    ]/@pArr
]


(* The rules to check fields' values *)
validators = AssociationThread[fields,
   StringMatchQ /@
    {p : DigitCharacter .. /; 1920 <= int[p] <= 2002, (* byr *)
     p : DigitCharacter .. /; 2010 <= int[p] <= 2020, (* iyr *)
     p : DigitCharacter .. /; 2020 <= int[p] <= 2030, (* eyr *)
     num : DigitCharacter .. ~~ unit : {"cm", "in"} /; Which[
       unit == "cm", 150 <= int[num] <= 193,
       unit == "in", 59 <= int[num] <= 76
       ], (* hgt *)
     "#" ~~ Repeated[HexadecimalCharacter, {6}], (* hcl *)
     {"amb", "blu", "brn", "gry", "grn" , "hzl", "oth"}, (* ecl *)
     Repeated[DigitCharacter, {9}], (* pid *)
     ___ (* cid *)
     }
   ];


(* Functions to check whether a passport is valid 
   1. contains all the required fields
   2. validates the fields' values
*)
checkField[field_,value_]:= validators[field][value]

checkRequired[passport_]:=
  SubsetQ[Keys@passport,Keys@Select[reqs,TrueQ]]

validatePassport[passport_]:=
  checkRequired[passport] && And@@KeyValueMap[checkField,passport]


Print["--- Part 1 ---"]

pOk = checkRequired /@ passports // Count[True];
Print["There are "~~ToString[pOk]~~" passports with all the required fields"]

Print["--- Part 2 ---"]
pValid = validatePassport /@ passports // Count[True];
Print["There are "~~ToString[pValid]~~" valid passports (all fields verified)"]
