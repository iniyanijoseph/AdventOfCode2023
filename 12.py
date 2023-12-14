# aoc 2023 _.py

import pathlib
import sys

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
    numbers = [[line.split(" ")[0], list(map(int, line.split(" ")[1].split(",")))] for line in numbers]

    s = 0

    for strings, springs in numbers:
        for i in range(len(strings)):
            s += recursivelyFit(strings, springs, [False for n in strings], i, 0)
    
    return s
    print("EO1____________")

def recursivelyFit(line, springs, fitted, index, numFitted):
    if(index > len(line)):
        return 0
    if(numFitted == len(springs)):
        return 1

    fitting = springs[numFitted + 1]
    
    s = 0

    for i in range(index, len(line)):
        canFit = (i + fitting < len(line))and all([line[j] != "." for j in range(i, i+fitting)])
        if(not canFit):
            return 0
        else:
            pre = fitted[0:i]
            l = [True for i in range(fitting)]
            post = fitted[fitting+i:]
            nFit = pre + l + post
            s += recursivelyFit(line,
                  springs,
                  nFit,
                  fitting + i+2,
                  numFitted + 1)
    return s


def part2(numbers):
    """Solve part 2."""
    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(12)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))