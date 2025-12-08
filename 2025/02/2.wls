#!/usr/bin/env wolframscript
(* AoC day 2, 2025: Gift Shop *)

(* Load packages *)
$packagesDir = FileNameJoin[{DirectoryName[$InputFileName], "..", "packages"}];
PacletDirectoryLoad[$packagesDir];
Needs["StringUtilities`"];

(* Read input *)
input = $ScriptInputString;

(* Parse ranges: "start-end,start-end,..." *)
ranges = IntegerList["-"] /@ StringSplit[input, ","];

(* Helper: valid pattern lengths for a k-digit number *)
(* Pattern length p must divide k and repeat at least twice (k/p >= 2) *)
validPatterns[k_] := Select[Divisors[k], k/# >= 2 &]

(* Multiplier for pattern of length p in a k-digit number *)
(* E.g., 121212 = 12 * 10101 where 10101 = (10^6 - 1)/(10^2 - 1) *)
multiplier[k_, p_] := (10^k - 1)/(10^p - 1)

(* Check if n is an "invalid" ID (made of repeating pattern) *)
invalidQ[n_Integer] := With[{k = IntegerLength[n]},
  AnyTrue[validPatterns[k], IntegerQ[n/multiplier[k, #]] && n/multiplier[k, #] < 10^# &]
]

(* Part 1: Sum of all invalid IDs in ranges *)
(* TODO: This solution approach is incomplete in the notebook *)
(* The notebook shows the mathematical approach but not the full implementation *)
part1 = "TODO";
Print[part1]

(* Part 2 *)
part2 = "TODO";
Print[part2]
