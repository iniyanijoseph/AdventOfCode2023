# aoc 2023 8.py

import re
from math import gcd


def parse(puzzle_input):
    """Parse input."""
    # Read each line as a string
    file = open(f'{puzzle_input}.txt',mode='r')
    inp = file.read().split("\n")
    inp = [re.split("\W+", line) for line in inp]
    inp.remove([''])
    file.close()

    # Convert each line to an integer 
    # inp = list(map(lambda x : int(x) if x != "" else -1, inp))
    
    return inp

def part1(numbers):
    """Solve part 1."""
    instructions = numbers[0][0].replace("L", "0").replace("R", "1")
    k = 0
    nodes = numbers[1:]
    adjacency = {}
    for node in nodes:
        if not node[0] in adjacency:
            adjacency[node[0]] = [node[1], node[2]]
    
    curr = "AAA"
    s = 0
    while(curr != "ZZZ"):
        s += 1
        curr = adjacency[curr][int(instructions[k])]
        k = (k+1)%len(instructions)
    return s
    print("EO1____________")

def part2(numbers):
    """Solve part 2."""
    instructions = numbers[0][0].replace("L", "0").replace("R", "1")
    nodes = numbers[1:]
    adjacency = {}
    for node in nodes:
        if not node[0] in adjacency:
            adjacency[node[0]] = [node[1], node[2]]
    
    starts = []
    for node in nodes:
        if re.search("\w{2}A", node[0]):
            starts.append(node[0])
    
    s = [0 for n in starts]

    for ind, curr in enumerate(starts):
        k = 0
        while(not re.search("\w{2}Z", curr)):
            s[ind] += 1
            curr = adjacency[curr][int(instructions[k])]
            k = (k+1)%len(instructions)
    
    lcm = 1
    for i in s:
        lcm = lcm*i//gcd(lcm, i)

    return lcm

    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(8)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))