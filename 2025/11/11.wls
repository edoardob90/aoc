#!/usr/bin/env wolframscript
(* ::Package:: *)

(* AoC day 11, 2025: Reactor *)

(* Timing function *)
SetAttributes[Timer, {HoldAll}];
Timer[expr_] := Block[{result},
  ClearSystemCache[];
  result = RepeatedTiming[expr];
  Print["Time: ", UnitConvert[Quantity[First@result, "Seconds"], "Conventional"]];
  Last[result]
]

(* Read input *)
input = StringSplit[$ScriptInputString, "\n"];

(* Build directed graph from input *)
graph = StringCases[input,
  from__ ~~ ": " ~~ to__ :> Thread[from \[DirectedEdge] StringSplit[to]]
] // Flatten // Graph;

(* Part 1: Count all paths from "you" to "out" *)
part1 = FindPath[graph, "you", "out", Infinity, All] // Length;
Print[part1]


(* Part 2: Count paths going through both "fft" and "dac"

   If A is the adjacency matrix of a DAG, then (I - A)^-1
   counts paths between vertices. Entry (i,j) gives the number of paths from i to j.

   We need paths: svr -> fft -> dac -> out  AND  svr -> dac -> fft -> out
   pathCount multiplies the relevant matrix entries along each path.
*)

pathCount[m_, path_List] := Times @@ (m[[#1, #2]] & @@@ Partition[path, 2, 1]);

part2a = Timer @ With[{n = VertexCount@graph},
  Module[{s, f, d, o, m = Inverse[IdentityMatrix[n] - AdjacencyMatrix[graph]]},
    {s, f, d, o} = VertexIndex[graph, #] & /@ {"svr", "fft", "dac", "out"};
    pathCount[m, {s, f, d, o}] + pathCount[m, {s, d, f, o}]
  ]
];
Print[part2a]


(* Part 2b: Optimized using LinearSolve instead of full matrix inversion

   We only need columns {f, d, o} of (I - A)^-1.
   Solving (I - A) * x = e_j gives the j-th column of M.

   After computing cols = [col_f, col_d, col_o], we extract:
   - Path svr->fft->dac->out needs: M[s,f], M[f,d], M[d,o] = cols[[{s,f,d}, {1,2,3}]]
   - Path svr->dac->fft->out needs: M[s,d], M[d,f], M[f,o] = cols[[{s,d,f}, {2,1,3}]]

   Note that the column indices must be swapped!
   Why? Column 1 is col_f (paths TO fft), column 2 is col_d (paths TO dac), column 3 is col_o (paths TO out)
   
   So, the elements we need from the columns matrix are:
   - For svr->fft->dac->out: we need M[s,f] from col 1, M[f,d] from col 2, M[d,o] from col 3 (default ordering)
   - For svr->dac->fft->out: we need M[s,d] from col 2, M[d,f] from col 1, M[f,o] from col 3 (swap 1 and 2)
*)

part2b = Timer @ With[{n = VertexCount@graph},
  Module[{s, f, d, o, M = IdentityMatrix[n, SparseArray] - AdjacencyMatrix[graph], cols},
    {s, f, d, o} = VertexIndex[graph, #] & /@ {"svr", "fft", "dac", "out"};
    cols = Transpose@Map[LinearSolve[M], UnitVector[n, #] & /@ {f, d, o}];
    Times @@ Diagonal[cols[[{s, f, d}, {1, 2, 3}]]] +
    Times @@ Diagonal[cols[[{s, d, f}, {2, 1, 3}]]]
  ]
];
Print[part2b]
