#!/usr/bin/env wolframscript
(* ::Package:: *)

int = Interpreter["Integer"];
input = int /@ StringSplit[$ScriptInputString, "\n"];

(* Function to check if a number is valid, that is,
 at least a pair of numbers in the preceding 25 sum to it *)
 validNumberQ[input_,pre_,num_]:=
  If[!MemberQ[input,num],
    Print[ToString@num~~" is not in input!"]; False,  
    With[{pos=Position[input,num] /. List->Sequence},
	If[pos>pre,
	  MemberQ[Total/@Subsets[input[[(pos-pre);;(pos-1)]],{2}],num],
		True]
  ]
]

badNumber = Catch[
    Scan[If[!validNumberQ[input, 25,#], Throw[#]]&, input]
    ];
Print["--- Part 1 ---\nThe bad number is ", ToString@NumberForm[badNumber, DigitBlock->3,NumberSeparator->" "]]

f[input_List, target_Integer, n_Integer:1, m_Integer:1]:=
  With[{k=Min[m,Length[input]]}, (* ensures tha j \[LessEqual] length of input *)
   With[{sum=Total@input[[n;;k]]},
    Which[
       (* found the range! *)
       sum==target,input[[n;;k]],
      (* wider range *)
      sum<target, f[input,target, n, k+1], 
      (* narrower range, but be careful to input[[i;;j]] with i>j! *)
      sum>target, f[input,target, n+1, Max[n+1,k]]
    ]
  ]
]

range = f[input, badNumber];
Print["\n--- Part 2 ---\nEncryption weakness is "~~ToString@NumberForm[Total@MinMax@range,DigitBlock->3,NumberSeparator->" "]]
