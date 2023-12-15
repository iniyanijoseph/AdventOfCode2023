# aoc 2023 9.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    # Read each line as a string
    file = open(f'{puzzle_input}.txt',mode='r')
    inp = file.read().split("\n")
    inp = [list(map(int, line.split(" "))) for line in inp]
    file.close()

    # Convert each line to an integer 
    # inp = list(map(lambda x : int(x) if x != "" else -1, inp))
    
    return inp

def part1(numbers):
    """Solve part 1."""
    s = 0
    for line in numbers:
        while not all([n == 0 for n in line]):
              s += line[-1]
              line = [line[n+1]-line[n] for n in range(len(line) - 1)]
    return s
    print("EO1____________")

def part2(numbers):
    """Solve part 2."""
    s = 0
    for line in numbers:
        hist = []
        while not all([n == 0 for n in line]):
            hist += [line]
            line = [line[n+1]-line[n] for n in range(len(line) - 1)]
        hist += [line]
        
        hist = hist[::-1]

        hist[0].append(0)

        for i in range(1, len(hist)):
            hist[i] = [hist[i][0] - hist[i-1][0]] + hist[i]
        
        s += hist[-1][0]
    

    return s
    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(9)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))