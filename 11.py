# aoc 2023 11.py

import pathlib
import sys
import re

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
    rows = [all([i != "#" for i in k]) for k in numbers]
    transposed = [[numbers[j][i] for j in range(len(numbers))] for i in range(len(numbers[0]))]
    cols = [all([i != "#" for i in k]) for k in transposed]

    s = 0

    pairs = []

    for x, i in enumerate(numbers):
        for y, j in enumerate(i):
            if(j == "#"):
                pairs.append((x, y))
    #print(pairs)

    for pair in pairs:
        for other in pairs:
            diff = abs(other[0]-pair[0]) + abs(other[1]-pair[1])
            #re = rows[min(other[0], pair[0]):max(other[0], pair[0])]
            numberRowExpansions = sum(rows[min(other[0], pair[0]):max(other[0], pair[0])])
            #ce = cols[min(other[1], pair[1]):max(other[1], pair[1])]
            numberColExpansions = sum(cols[min(other[1], pair[1]):max(other[1], pair[1])])

            #print(pair, other, sum([diff, numberRowExpansions, numberColExpansions]))
            s += sum([diff, numberRowExpansions, numberColExpansions])
    
    return s//2
    print("EO1____________")

def part2(numbers):
    """Solve part 2."""
    rows = [all([i != "#" for i in k]) for k in numbers]
    transposed = [[numbers[j][i] for j in range(len(numbers))] for i in range(len(numbers[0]))]
    cols = [all([i != "#" for i in k]) for k in transposed]

    s = 0

    pairs = []

    for x, i in enumerate(numbers):
        for y, j in enumerate(i):
            if(j == "#"):
                pairs.append((x, y))

    for pair in pairs:
        for other in pairs:
            diff = abs(other[0]-pair[0]) + abs(other[1]-pair[1])
            numberRowExpansions = sum(rows[min(other[0], pair[0]):max(other[0], pair[0])])
            numberColExpansions = sum(cols[min(other[1], pair[1]):max(other[1], pair[1])])

            mult = (1E6) -1 

            s += sum([diff, numberRowExpansions*mult, numberColExpansions*mult])    

    return s//2
    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(11)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))