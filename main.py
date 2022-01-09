#!/usr/bin/python3
# This file count charackers from stdin.
import sys
line = "\n"
stat = {}
max = 0
min = 9999
total = 0
while "\n" in line:
    line = sys.stdin.readline().lower()
    for c in line:
        if c not in stat:
            stat[c] = 0
        if ord(c) > max:
            max = ord(c)
        if ord(c) < min:
            min = ord(c)
        stat[c] +=1
        total +=1

for i in range(min,max):
    if chr(i) in stat and i> 96 and i < 512:
        print("{} {} {} {}".format(
            stat[chr(i)],
            round(100*stat[chr(i)]/total,3),
            chr(i),
            i)
        )
