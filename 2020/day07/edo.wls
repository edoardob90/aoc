#!/usr/bin/env wolframscript
(* ::Package:: *)

int = Interpreter["Integer"];
bag = FixedOrder[WordCharacter..,Whitespace,WordCharacter..];

input = StringSplit[$ScriptInputString,"\n"]//StringReplace["no other"->"0"];

ClearAll[lookupBag]
(* lookup bags that contains a child *)
lookupBag[list_][child_]:=Union@@Map[StringCases[StartOfLine~~parent:bag~~__~~"contain"~~__~~num:DigitCharacter~~__~~child :> parent->int[num]],list]
(* lookup a specific parent bag that contains child *)
lookupBag[list_][parent_,child_:"shiny gold"]:=
Union@@Map[StringCases[StartOfLine~~parent~~__~~"contain"~~__~~num:DigitCharacter~~__~~child :> parent->int[num]],list]

bagsWithSG=FixedPointList[
            First/@Union@@lookupBag[input]/@#&, First/@lookupBag[input]["shiny gold"]] // Apply@Union // Length

Print["--- Part 1 ---\nNumber of colors (bags) with a shiny gold bag: "~~ToString@bagsWithSG]
