#!/usr/bin/env wolframscript
(* ::Package:: *)

int = Interpreter["Integer"];


Print["Part 1\n"]
nPwdOk = StringCases[$ScriptInputString,
d1:DigitCharacter..~~"-"~~d2:DigitCharacter..~~" "~~lc:LetterCharacter~~": "~~str:LetterCharacter.. :> 
int[d1] <= StringCount[str,lc]<=int[d2]
]//Count[True];
Print["There are "~~ToString[nPwdOk]~~" valid password\n"]


Print["Part 2\n"]
nPwdOk = Map[
Count[#[[1]],#[[2]]]&,
StringCases[$ScriptInputString,
d1:DigitCharacter..~~"-"~~d2:DigitCharacter..~~" "~~lc:LetterCharacter~~": "~~str:LetterCharacter.. :> 
{StringPart[str,{int[d1],int[d2]}],lc}]]//Count[1];

Print["There are "~~ToString[nPwdOk]~~" valid password\n"]
