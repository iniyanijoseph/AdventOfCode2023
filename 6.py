# aoc 2023 _.py

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
    time = list(map(int, (re.split("\s+", numbers[0])[1:])))
    dist = list(map(int, (re.split("\s+", numbers[1])[1:])))


    pairs = [(time[i], dist[i]) for i in range(len(time))]

    a = []

    for pr in pairs:
        s = 0
        for i in range(pr[0]):
            distance = (pr[0] - i)*i
            if(distance > pr[1]):
                s+= 1
        a.append(s)
    
    k = 1
    for r in a:
        k *= r
    return k

    print("EO1____________")

def part2(numbers):
    """Solve part 2."""
    time = list(map(int, (re.split("\s+", numbers[0])[1:])))
    time = [int(''.join(list(map(str, time))))]
    dist = list(map(int, (re.split("\s+", numbers[1])[1:])))
    dist = [int(''.join(list(map(str, dist))))]

    pairs = [(time[i], dist[i]) for i in range(len(time))]

    a = []

    for pr in pairs:
        s = 0
        for i in range(pr[0]):
            distance = (pr[0] - i)*i
            if(distance > pr[1]):
                s+= 1
        a.append(s)
    
    k = 1
    for r in a:
        k *= r
    return k

    print("EO2____________")y 
if __name__ == "__main__":
    numbers = parse(6)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))