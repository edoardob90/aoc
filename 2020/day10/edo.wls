#!/usr/bin/env wolframscript
(* ::Package:: *)

input = FromDigits/@StringSplit[$ScriptInputString, "\n"];

joltsCounts = 
   Partition[
   (* We need both 0 and the last element+3 in the list *)
     Join[{0}, input, {Max[input+3]}] //
     (* Sort the list, then partition in pairs with a offset of 1 *)
        Sort, 2, 1] //
     (* We subtract the last-first elements of each pair *)
        Map[Reverse/*Apply[Subtract]] // 
     (* Count how many 1,2,3 differences we have *)
        Tally // 
     (* Take the last element (the actual count) of each pair
        and multiply them together *)
        Map[Last] // Apply@Times
