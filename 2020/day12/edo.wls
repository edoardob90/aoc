#!/usr/bin/env wolframscript
(* ::Package:: *)

directions = StringSplit[$ScriptInputString,"\n"];

(* ::Subsection:: *)
(*Part 1*)

(* ::Text:: *)
(*The initial coordinate is {{0,0}, {"E", "S", "W", "N"}} because the ship is facing East.*)

initCoord = {{0,0},{"E", "S", "W", "N"}};

(* ::Text:: *)
(*This is a convention for axes*)

axes = <|"N"->{0,1},"E"->{1,0},"S"->{0,-1},"W"->{-1,0}|>;

readNav[coord_, s_]:=
Block[{dir,arg,x,y,facing},
{{x,y}, facing} = coord;
{dir, arg} = First@StringCases[s,a:LetterCharacter~~b:DigitCharacter..:>{a,FromDigits@b}];
Switch[dir,
  "N",{{x,y+arg},facing},
  "S",{{x,y-arg},facing},
  "W",{{x-arg,y},facing},
  "E",{{x+arg,y},facing},
  "R",{{x,y},RotateLeft[facing,Quotient[arg,90]]},
  "L",{{x,y},RotateRight[facing,Quotient[arg,90]]},
  "F",{{x,y}+arg*axes[facing[[1]]],facing}
]
]

p1=FoldList[readNav, initCoord, directions];
Print[StringTemplate["--- Part 1 ---\nManhattan distance covered by the ship: ``"][ManhattanDistance[p1[[1,1]], p1[[-1,1]]]]]

(* ::Subsection:: *)
(*Part 2*)

(* ::Text:: *)
(*The instructions indicate how to move a waypoint relative to the ship. It's easy to adapt the N-S-E-W instructions since they simply move the waypoint's coordinates, {Subscript[x, w],Subscript[y, w]}. *)
(*The rotations get a bit trickier: we have to rotate the waypoint around the ship by the given number of degrees. "L" means counter-clockwise, "R" clockwise.*)

(* ::Text:: *)
(*The waypoint is initially at 10 east, 1 north of the ship.*)

initWayp={10,1};
initShip={0,0};

(* ::Text:: *)
(*Remember: the waypoint's coordinate are relative to the ship, therefore the rotation of {Subscript[x, w],Subscript[y, w]} is as if it were around the origin!*)

readNavWp[coords_,s_]:=
Block[{dir,arg,x,y,xw,yw},
{{x,y},{xw,yw}}=coords;
{dir,arg}=First@StringCases[s,a:LetterCharacter~~b:DigitCharacter..:>{a, FromDigits@b}];
Switch[dir,
  "N",{{x,y},{xw,yw+arg}},
  "S",{{x,y},{xw,yw-arg}},
  "W",{{x,y},{xw-arg,yw}},
  "E",{{x,y},{xw+arg,yw}},
  "R",{{x,y},RotationTransform[-arg Degree][{xw,yw}]},
  "L",{{x,y},RotationTransform[arg Degree][{xw,yw}]},
  "F",{{x,y}+arg{xw,yw},{xw,yw}}
 ]
]

p2=FoldList[readNavWp, {initShip, initWayp}, directions];
Print[StringTemplate["\n--- Part 2 ---\nManhattan distance covered by the ship: ``"][ManhattanDistance[p2[[1,1]], p2[[-1,1]]]]]
