#!/usr/bin/env wolframscript
(* ::Package:: *)

int = Interpreter["Integer"];
ops = {"acc","jmp","nop"};

(* parse a single line as one instruction *)
readInstruction[line_String]:=
First@StringCases[line,o:ops~~" "~~s:"+"|"-"~~n:DigitCharacter..:>o->int[s~~n]]

bootCode = Association/@readInstruction/@StringSplit[$ScriptInputString, "\n"];

execInstruction[inst_Association]:=
With[{k=First@Keys@inst,v=First@Values@inst},
++numExecs[k];
Switch[k,
"nop",AddTo[globalIndex,1],
"acc",AddTo[globalCount,v];AddTo[globalIndex,1],
"jmp",AddTo[globalIndex,v]
];
{globalIndex,globalCount}
]

globalCount=0;
globalIndex=1;
numExecs = AssociationThread[ops,{0,0,0}];
(* the element before the last contains the global index and the
accumulator value before the bootcode enters the infinite loop *)
stop = NestWhileList[
   execInstruction[bootCode[[#[[1]]]]]&, 
   {globalIndex,globalCount},
   DuplicateFreeQ[List[##][[All,1]]]&, All][[-2]];

Print["--- Part 1 ---\nAccumulator = "~~ToString@Last@stop~~
       " and instruction index = "~~ToString@First@stop]
