# aoc 2023 12.py

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
        k = 0
        for i in range(len(strings)):
            k += recursivelyFit(strings, springs, i, 0)
        s += k
        print(k)
    
    return s
    print("EO1____________")

def recursivelyFit(line, springs, index, current):
    end = index + springs[current]
    if(end > len(line)):
        return 0
    group = line[index:end]
    if(not all([r != "." for r in group]) or (line[index-1] == "#" and index != 0) or (end < len(line) and line[end] == "#")):
        return 0
    elif(current == len(springs)-1):
        return 1


    s = 0

    for i in range(end+1, len(line)):
        s += recursivelyFit(line, springs, i, current+1)
    
    return s


def part2(numbers):
    """Solve part 2."""
    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(12)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))