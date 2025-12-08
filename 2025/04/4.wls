#!/usr/bin/env wolframscript
(* AoC day 4, 2025: Printing Department *)

(* Load packages *)
$packagesDir = FileNameJoin[{DirectoryName[$InputFileName], "..", "packages"}];
PacletDirectoryLoad[$packagesDir];
Needs["StringUtilities`"];
Needs["GridUtilities`"];

(* Read input *)
input = $ScriptInputString;
grid = MakeGrid[input];

(* Part 1: Count paper rolls (@) with fewer than 4 adjacent rolls *)
(* A roll is accessible if < 4 of its 8 neighbors (Moore) are also rolls *)
part1 = Length@Select[
  GridPositions[grid, "@"],
  Count[Neighbors[#, grid, "Connectivity" -> Moore], "@"] < 4 &
];
Print[part1]

(* Part 2: Remove accessible rolls iteratively until no more can be removed *)
(* Count total rolls removed *)

(* Check if a roll at position can be removed (< 4 adjacent rolls) *)
removableQ[neighbors_List] := Count[neighbors, "@"] < 4

(* Remove all currently accessible rolls *)
removeAccessible[g_List] := With[
  {toRemove = Select[
    GridPositions[g, "@"],
    removableQ[Neighbors[#, g, "Connectivity" -> Moore]] &
  ]},
  ReplacePart[g, Thread[toRemove -> "."]]
]

(* Apply removal until fixed point *)
finalGrid = FixedPoint[removeAccessible, grid];
part2 = GridCount[grid, "@"] - GridCount[finalGrid, "@"];
Print[part2]
