#!/usr/bin/env wolframscript
(* ::Package:: *)

groups=StringSplit[$ScriptInputString, StartOfLine~~EndOfLine] // 
         Map[StringSplit[#,"\n"]&];

(* a bit redundant the Split & Join; I can find a more elegant line *)
anyYes = Length@*Keys@*LetterCounts/@StringJoin/@groups//Total;

Print["--- Part 1 ---\nCounts of answered questions in all groups: "~~
        ToString@anyYes]

(* Part 2: count only those answers to each everyone answered "yes" *)
everyYes = Map[Apply[Intersection]/*Length, 
              Map[LetterCounts/*Keys, groups, {2}]] // Total;
Print["--- Part 2 ---\nCounts of questions answered by everyone: "~~
        ToString@everyYes]
