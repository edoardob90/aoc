#!/usr/bin/env wolframscript

input = StringSplit[$ScriptInputString, "\n"];

(* Part 1 *)

part1 = #[[{1, -1}]]& /* FromDigits /@ StringCases[input, x:DigitCharacter :> ToExpression @ x] // Total;

Print[part1]

(* Part 2 *)

findLetterDigits[s_String] :=
    With[{numberRules = Thread[IntegerName /@ Range[9] -> Range[9]]},
        ToExpression /@ (StringTake[s, StringPosition[s, Join[ToString/@ Range[9], IntegerName[Range[9]]]]] /. numberRules)
    ]

part2 = #[[{1, -1}]]& /* FromDigits /@ findLetterDigits /@ input // Total;

Print[part2]
