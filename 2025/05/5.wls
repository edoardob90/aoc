#!/usr/bin/env wolframscript
(* AoC day 5, 2025: Cafeteria *)

(* Load packages *)
$packagesDir = FileNameJoin[{DirectoryName[$InputFileName], "..", "packages"}];
PacletDirectoryLoad[$packagesDir];
Needs["StringUtilities`"];

(* Read input *)
input = $ScriptInputString;

(* Parse: first section is ranges, second is ingredient IDs *)
{rangeLines, ingredientLines} = SplitLines /@ SplitLines[input, 2];

(* Parse ranges as list of {start, end} pairs, create Interval *)
ranges = IntegerList["-"] /@ rangeLines;
intervals = Apply[Interval, ranges];

(* Parse ingredient IDs *)
ingredients = FromDigits /@ ingredientLines;

(* Part 1: Count how many ingredients are fresh (in any range) *)
part1 = Count[IntervalMemberQ[intervals, ingredients], True];
Print[part1]

(* Part 2: Total number of fresh IDs (size of merged intervals) *)
(* Interval automatically merges overlapping ranges *)
part2 = Total[(#[[2]] - #[[1]] + 1) & /@ (List @@ intervals)];
Print[part2]
