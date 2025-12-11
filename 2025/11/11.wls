#!/usr/bin/env wolframscript
(* AoC day 11, 2025: Reactor *)

(* Read input *)

input = StringSplit[$ScriptInputString, "\n"];

(* Build directed graph from input *)
graph = StringCases[input,
  from__ ~~ ": " ~~ to__ :> Thread[from \[DirectedEdge] StringSplit[to]]
] // Flatten // Graph;

(* Part 1: Count all paths from "you" to "out" *)

part1 = FindPath[graph, "you", "out", Infinity, All] // Length;

Print[part1]


(* Part 2: Count paths going through both "fft" and "dac" *)

pathCount[m_, path_List] := Times @@ (m[[#1, #2]] & @@@ Partition[path, 2, 1]);

part2 = With[{n = VertexCount@graph},
  Module[{s, f, d, o, M = IdentityMatrix[n, SparseArray] - AdjacencyMatrix[graph], cols},
    {s, f, d, o} = VertexIndex[graph, #] & /@ {"svr", "fft", "dac", "out"};
    cols = Transpose@Map[LinearSolve[M], UnitVector[n, #] & /@ {f, d, o}];
    Times @@ Diagonal[cols[[{s, f, d}, {1, 2, 3}]]] +
    Times @@ Diagonal[cols[[{s, d, f}, {2, 1, 3}]]]
  ]
];

Print[part2]
