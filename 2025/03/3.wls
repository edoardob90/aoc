#!/usr/bin/env wolframscript
(* AoC day 3, 2025: Lobby *)

(* Load packages *)
$packagesDir = FileNameJoin[{DirectoryName[$InputFileName], "..", "packages"}];
PacletDirectoryLoad[$packagesDir];
Needs["StringUtilities`"];

(* Read input *)
input = $ScriptInputString;

(* Parse: each line is a battery bank, each character is a digit *)
banks = IntegerList[] /@ SplitLines[input];

(* Find largest number by picking maxLen digits greedily *)
(* At each step, pick the largest digit from valid range *)
largestNumber[digits_List, maxLen_Integer] :=
  With[{n = Length@digits},
    Reap[
      Fold[
        Module[{search, max, relPos},
          search = digits[[#1 ;; n - maxLen + #2]];
          max = Max[search];
          Sow[max];
          relPos = FirstPosition[search, max][[1]];
          #1 + relPos
        ] &,
        1,
        Range[maxLen]
      ]
    ][[2, 1]] // FromDigits
  ]

(* Part 1: Sum of largest 2-digit numbers from each bank *)
part1 = Total[largestNumber[#, 2] & /@ banks];
Print[part1]

(* Part 2: Sum of largest 12-digit numbers from each bank *)
part2 = Total[largestNumber[#, 12] & /@ banks];
Print[part2]
