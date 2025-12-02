#!/usr/bin/bash
num=( $(cat input.txt) ); for (( i=0; i<${#num[@]}; i++ )); do for n in ${num[@]}; do [[ $n ]] || continue; [[ $((${num[$i]} + ${n})) == 2020 ]] && { echo "$((${num[$i]} * ${n}))"; break 2; }; done; done
