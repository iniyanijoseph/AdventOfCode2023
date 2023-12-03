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
    print("EO1____________")

def part2(numbers):
    """Solve part 2."""
    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(15)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))