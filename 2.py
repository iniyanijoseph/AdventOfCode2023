# aoc 2023 2.py

import pathlib
import sys
from parse import compile
from parse import search

def parse(puzzle_input):
    """Parse input."""
    # Read each line as a string
    file = open(f'{puzzle_input}.txt',mode='r')
    inp = file.read().split("\n")
    file.close()

    # Convert each line to an integer 
    # inp = list(map(lambda x : int(x) if x != "" else -1, inp))
    
    return inp

def part1(numbers):
    """Solve part 1."""
    p = compile("Game {n:d}:")
    b = compile("{k:d} blue")
    g = compile("{l:d} green")
    r = compile("{r:d} red")
    s = 0
    for line in numbers:
        idnum = p.search(line)["n"]
        parts = line[8:].split(";")
        valid = True
        for part in parts:
            ru = (r.search(part)["r"] if r.search(part) != None else -1)
            gu = (g.search(part)["l"] if g.search(part) != None else -1)
            bu = (b.search(part)["k"] if b.search(part) != None else -1)

            if ru > 12 or gu > 13 or bu > 14:
                valid = False
        if(valid):
            s+=idnum
    return s
    print("EO1____________")

def part2(numbers):
    """Solve part 2."""
    b = compile("{k:d} blue")
    g = compile("{l:d} green")
    r = compile("{r:d} red")
    s = 0
    for line in numbers:
        parts = line[8:].split(";")
        rmx = -1
        gmx = -1
        bmx = -1
        for part in parts:
            ru = (r.search(part)["r"] if r.search(part) != None else -1)
            gu = (g.search(part)["l"] if g.search(part) != None else -1)
            bu = (b.search(part)["k"] if b.search(part) != None else -1)

            rmx = max(ru, rmx)
            bmx = max(bu, bmx)
            gmx = max(gu, gmx)

        s+=rmx*bmx*gmx 
    return s
    print("EO1____________")
    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(2)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))