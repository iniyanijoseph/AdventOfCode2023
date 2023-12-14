# aoc 2023 _.py

import pathlib
import sys
import numpy as np

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
    numbers =[[row[i] for row in numbers] for i in range(len(numbers[0]))]
    for row in numbers:
        lastSeenRock = -1
        for i, ele in enumerate(row):
            if ele == "O":
                try:
                    row[i] = "."
                    row[lastSeenRock+1] = "O"
                    lastSeenRock += 1
                except:
                    pass
            if ele == "#":
                lastSeenRock = i
    numbers =[[row[i] for row in numbers] for i in range(len(numbers[0]))]
    
    s = 0

    for i, ele in enumerate(numbers):
        numOs = sum([i == "O" for i in ele])
        s += numOs * (len(numbers)-i)
        
    return s

def part2(numbers):
    """Solve part 2."""
    states = []
    numCycles = 0

    while(not numbers in states):
        states.append(numbers)

        for i in range(4):
            numbers =[[row[i] for row in numbers] for i in range(len(numbers[0]))]
            for row in numbers:
                lastSeenRock = -1
                for i, ele in enumerate(row):
                    if ele == "O":
                        try:
                            row[i] = "."
                            row[lastSeenRock+1] = "O"
                            lastSeenRock += 1
                        except:
                            pass
                    if ele == "#":
                        lastSeenRock = i
            numbers =[[row[i] for row in numbers] for i in range(len(numbers[0]))]
            numbers = list(zip(*numbers[::-1]))
        numCycles+=1

    st = states.index(numbers)
    numCyc = (1000000000 - st) % (numCycles - st) + st
    numbers = states[numCyc]

    """
    |-----------------------s--------e|
    """

    s = 0

    for i, ele in enumerate(numbers):
        numOs = sum([i == "O" for i in ele])
        s += numOs * (len(numbers)-i)

    return s

    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(14)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))