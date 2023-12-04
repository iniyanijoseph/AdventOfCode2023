# aoc 2023 4.py

import pathlib
import sys
import copy
from collections import deque


def parse(puzzle_input):
    """Parse input."""
    # Read each line as a string
    file = open(f'{puzzle_input}.txt',mode='r')
    inp = file.read().split("\n")
    ids = [range(1, len(inp)+1)]
    inp = [line[line.find(":")+1::] for line in inp]
    inp = [line.split("|") for line in inp]

    file.close()
    # Convert each line to an integer 
    for i, line in enumerate(inp):
        line[0] = set(map(int, line[0].split()))
        line[1] = set(map(int, line[1].split()))
        line.append(i+1)

    return inp

def part1(numbers):
    """Solve part 1."""
    points = 0;
    for k in numbers:
        overlap = len(set.intersection(k[0], k[1]))
        points += 2**(overlap-1) if overlap > 0 else 0
    return points
    print("EO1____________")

def part2(numbers):
    """Solve part 2."""
    s = 0
    q = deque(numbers)
    while(len(q) > 0):
        curr = q.popleft()
        s+=1

        overlap = len(set.intersection(curr[0], curr[1]))
        for k in range(overlap):
            q.append(numbers[k+curr[2]])
        
    return s
    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(4)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))