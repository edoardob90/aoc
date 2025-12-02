#!/usr/bin/env wolframscript
(* ::Package:: *)

input = StringSplit[$ScriptInputString, "\n"];

(* ::Section:: *)
(*Part 1*)

(* ::Text:: *)
(*The Wolfram Language supports "infix" and "postfix" notation for operators.*)
(*We can exploit that by converting an expression like a+b with a~op~b*)

parseExpression[expr_String]:=
 ToExpression[
  StringReplace[expr,{"*" -> "~prod~", "+" -> "~sum~"}]]//
  ReplaceAll[{prod -> Times, sum -> Plus}]

sumP1 = Plus @@ parseExpression /@ input;
Print[
StringTemplate["--- Part 1 ---\nSum of all the expressions evaluated
  with equal precedence of sum and product:\n``"][sumP1]
 ]

(* ::Section:: *)
(*Part 2*)

(* ::Text:: *)
(*This is a bit more difficult, but what we have to do is inverting the precedence of product and sum operations.*)
(*In practice we do the following:*)

(* ::ItemNumbered:: *)
(*exchange all the sum with products*)

(* ::ItemNumbered:: *)
(*convert the string to a Wolfram Language expression. This interprets the expression by parenthesizing the expression as we normally would: first multiplications, then summations*)

(* ::ItemNumbered:: *)
(*keep this expression unevaluated with "HoldForm". We have to swap once again multiplications and summations that now have been interpreted with their corresponding operators "Times" and "Plus"*)

(* ::ItemNumbered:: *)
(*actually evaluate the expression with "ReleaseHold"*)

parseExprSumBeforeProd[expr_String]:=
ToExpression[
StringReplace[expr, {"*"->"+","+"->"*"}], (* swap x and + *)
 InputForm, (* ...as if we were writing a normal input *)
 HoldForm]// (* apply HoldForm to keep the expression unevaluated *)
 ReplaceAll[{Times->Plus,Plus->Times}] (* swap back *)

sumP2 = Plus @@ parseExprSumBeforeProd /* ReleaseHold /@ input;
Print[
StringTemplate["\n--- Part 2 ---\nSum of all the expressions evaluated
  with summations before multiplications:\n``"][sumP2]
 ]
