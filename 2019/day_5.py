#!/usr/bin/env pypy
"""
Day 5: Sunny with a Chance of Asteroids
https://adventofcode.com/2019/day/5
"""

import fileinput
import sys
from aoc import read_file

class Intcode():
    def __init__(self, init, input_value):
        if not isinstance(init, list):
            raise TypeError
        self.intcode = [int(x) for x in init]
        self.idx = 0 # instruction pointer
        self.input = input_value
        self.jump = True # by default, we always update the instruction pointer

    def reset(self, init, noun=12, verb=2):
        self.idx = 0
        self.intcode = [int(x) for x in init]
        self.intcode[1] = noun
        self.intcode[2] = verb

    def __len__(self):
        return len(self.intcode)

    def __getitem__(self, key):
        return self.intcode[key]

    def __setitem__(self, key, value):
        self.intcode[key] = value

    def __repr__(self):
        intcode_str = ''
        for i,v in enumerate(self.intcode):
            intcode_str += f'Intcode({i}) = {v}\n'
        return f'Intcode:\nLast idx = {self.idx}\n{intcode_str}'

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.intcode):
            raise StopIteration
        current = self.intcode[self.idx]
        self.idx += 1
        return current

    def read_mode(self, modes, args):
        # parameter modes: how do we interpret the args?
        # 0 => arg is ADDRESS (position mode)
        # 1 => arg is VALUE (immediate mode)
        values = []
        for i, v in enumerate(list(modes)[::-1]):
            print(i, v, args[i])
            if v is '0':
                values.append(self.intcode[args[i]])
            elif v is '1':
                values.append(args[i])
            else:
                raise RuntimeError
        return values

        #if m == '00':
        #    return (self.intcode[args[0]], self.intcode[args[1]])
        #elif m == '11':
        #    return (args[0], args[1])
        #elif m == '10':
        #    return (self.intcode[args[0]], args[1])
        #elif m == '01':
        #    return (args[0], self.intcode[args[1]])
        #else:
        #    raise RuntimeError

    def exec(self, opcode, modes, args):
        self.jump = True
        # which operation?
        if opcode == '01':
            x, y, _ = self.read_mode(modes, args)
            self.intcode[args[-1]] = x + y
            return True
        elif opcode == '02':
            x, y, _ = self.read_mode(modes, args)
            self.intcode[args[-1]] = x * y
            return True
        elif opcode == '03':
            self.intcode[args[-1]] = self.input
            return True
        elif opcode == '04':
            print(self.intcode[args[-1]])
            #print(f'Intcode[{args[-1]}] = {self.intcode[args[-1]]}')
            return True
        elif opcode == '99':
            return False
        elif opcode in ['05','06']:
            p0, p1, _ = self.read_mode(modes, args)
            if (opcode == '05' and p0 != 0) or (opcode == '06' and p0 == 0):
                self.jump = False
                self.idx = p1
            return True
        elif opcode in ['07','08']:
            p0, p1, _ = self.read_mode(modes, args)
            if (opcode == '07' and p0 < p1) or (opcode == '08' and p0 == p1):
                self.intcode[args[-1]] = 1
            else:
                self.intcode[args[-1]] = 0
            return True
        else:
            raise RuntimeError

    def read(self, inst):
         # how many args each instruction takes
        opcode_dict = {
            "99": 0,
            "01": 3,
            "02": 3,
            "03": 1,
            "04": 1,
            "05": 2,
            "06": 2,
            "07": 3,
            "08": 3
        }
        opcode = f'{inst:05d}'
        return (opcode[-2:], opcode[:-2], opcode_dict[opcode[-2:]])

    # Differences from day 2:
    #  - opcode is a string of length 5, padded with 0 if necessary
    #  - args are NOT always of length 4
    def process(self):
        status = True
        while status and self.idx < len(self.intcode):
            print(self.intcode, self.idx)
            opcode, modes, nargs = self.read(self.intcode[self.idx]) # read current instruction to determine opcode, args, and parameter modes
            args = self.intcode[self.idx + 1:self.idx + nargs + 1]
            print(opcode, [(i,j) for i,j in zip(modes,args)])
            status = self.exec(opcode, modes, args)
            # set the output
            self.output = self.intcode[0]
            # update instruction pointer?
            if self.jump:
                #print(f'Jumping {nargs+1}')
                self.idx += nargs + 1

if __name__ == '__main__':
    intcode_str = [x.strip() for x in fileinput.input()][0].split(',')

    #print("======= Intcode Diagnostic Run =======")
    #intcode = Intcode(intcode_str, input_value=1)
    #intcode.process()

    print("======== Part 2 ========")
    intcode = Intcode(intcode_str, input_value=4)
    intcode.process()
