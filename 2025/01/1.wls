#!/usr/bin/env wolframscript
(* AoC day 1, 2025: Secret Entrance *)

(* Read input *)
input = $ScriptInputString;

(* Helper *)
int = Interpreter["Integer"];

(* Parse rotations: L/R followed by digits -> signed offset *)
rotations = StringCases[input, f_ ~~ n : DigitCharacter .. :> Switch[f, "R", 1, "L", -1] int@n];

(* Part 1: Count how many times dial points at 0 after a rotation *)
positions = FoldList[Mod[#1 + #2, 100] &, 50, rotations];
part1 = Count[positions, 0];
Print[part1]

(* Part 2: Count all times dial passes through 0 (including during rotations) *)
(* Track: {current position, cumulative position (unwrapped), zero count} *)
part2 = With[{states = FoldList[
    With[{r = #1[[1]] + #2}, {Mod[r, 100], r, #1[[3]] + Abs[Quotient[r, 100]]}] &,
    {50, 50, 0},
    rotations
  ]},
  Last[states][[3]]
];
Print[part2]
