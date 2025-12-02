#!/usr/bin/env wolframscript
(* ::Package:: *)

initialMap = Characters@StringSplit[$ScriptInputString];

(* find the neighbors of one seat *)
center[seat_]:= seat[[2,2]]
neighs[seat_]:= Catenate@Delete[seat, {2,2}]

(* A Cellular Automaton solution with a custom rule *)
rule = {Switch[center[#],
     (* If free, check that we don't have any occupied seats around *)
       "L", If[Count[neighs[#], "#"] == 0, "#", "L"],
       "#", If[Count[neighs[#], "#"] >= 4, "L", "#"],
       _, "."]&, {}, {1, 1}};

evolveCA[rule_,init_]:= NestWhileList[
        CellularAutomaton[rule, {#,"."}, {{{1}}}]&, init, Not@*SameQ, 2]

iterations = evolveCA[rule, initialMap];

occupiedSeats = Count[Last@iterations, "#", 2];

Print["--- Part 1 ---"]
Print[
 StringTemplate["Number of occupied seats after `a` steps: `b`"][<|"a"->Length@iterations, "b"->occupiedSeats|>]
 ]
