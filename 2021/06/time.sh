#!/bin/bash
name=$(basename $1 .py)
for days in 80 90 100 110 120 130 150; do
    time=$(pypy $1 $days < sample.txt | grep 'Elapsed' | cut -d' ' -f3)
    echo "$days $time" >> ${name}.out
done
