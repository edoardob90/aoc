#!/usr/bin/env wolframscript
(* AoC day 6, 2025: Trash Compactor *)

(* Load packages *)
$packagesDir = FileNameJoin[{DirectoryName[$InputFileName], "..", "packages"}];
PacletDirectoryLoad[$packagesDir];
Needs["StringUtilities`"];

(* Read input *)
input = $ScriptInputString;

(* Part 1: Problems arranged horizontally, numbers stacked vertically *)
(* Last line contains operators (* or +), problems separated by space columns *)
Block[{lines, numbers, ops},
  lines = SplitLines[input];
  (* Split into number rows (all but last) and operator row *)
  {numbers, ops} = TakeDrop[lines, {1, -2}];
  (* Parse each row into tokens (split by whitespace) *)
  numbers = StringSplit[#, WhitespaceCharacter ..] & /@ numbers;
  ops = Flatten[StringSplit[#, WhitespaceCharacter ..] & /@ ops];
  (* Transpose to group numbers by problem, build and evaluate expressions *)
  part1 = Total[ToExpression /@ MapThread[StringRiffle, {Transpose@numbers, ops}]];
];
Print[part1]

(* Part 2: Read column-wise (vertical numbers in grid format) *)
Block[{gridPart, opsPart, columns},
  (* Split at double newline: grid section and operators section *)
  {gridPart, opsPart} = Flatten@StringCases[input,
    grid__ ~~ "\n\n" ~~ ops : ("*" | "+" | " ") .. :> {grid, ops}
  ];
  (* Parse grid: split by newlines, transpose to columns, remove spaces, join digits *)
  columns = Characters /@ StringSplit[gridPart, "\n"];
  columns = Transpose[columns];
  columns = Map[DeleteCases[" "] /* StringJoin, columns];
  (* Split into problems (empty string separates problems) *)
  columns = SequenceSplit[columns, {""}];
  (* Parse operators *)
  ops = StringSplit[opsPart];
  (* Build and evaluate expressions *)
  part2 = Total[ToExpression /@ MapThread[StringRiffle, {columns, ops}]];
];
Print[part2]
