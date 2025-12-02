#!/usr/bin/env wolframscript
(* ::Package:: *)

keys = {cardPubKey, doorPubKey} = Interpreter["Integer"] /@ StringSplit[$ScriptInputString, "\n"];

transform[subnum_,loopsize_]:=
 PowerMod[subnum, loopsize, 20201227]

(* ::Text:: *)
(*We can brute-force the search for the loop size of both public keys because the prime number 20201227 is very small*)

findLoopSize[key_]:=
 Module[{lp=0},
  While[PowerMod[7, lp, 20201227] != key,
  ++lp
  ];
  lp
]

{lpCard, lpDoor} = findLoopSize /@ keys

encryption = transform[cardPubKey, lpDoor]
Print[StringTemplate["Encryption key is ``"][encryption]]

(* ::Text:: *)
(*Encryption keys must be equal*)

Print[ToString[encryption === transform[doorPubKey, lpCard]]]
