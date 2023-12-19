# aoc 2023 16.py

import pathlib
import sys
sys.setrecursionlimit(10000000)

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
    visited = [[False for i in r] for r in numbers]
    recurOne(numbers, 0, 0, visited, 1, [[set() for i in r] for r in numbers])
    return sum([sum(r) for r in visited])
    print("EO1____________")

def recurOne(numbers, row, col, visited, direction, dirs):
    if (not (0 <= row < len(numbers)) or not (0 <= col < len(numbers[0]))):
        return 
    if(direction in dirs[row][col] and visited[row][col]):
        return
    
    dirs[row][col].add(direction)
    visited[row][col] = True
    # 1 is R
    # -1 is L
    # 2 is U
    # 3 is D
    if(direction == -1 or direction == 1):
        if(numbers[row][col] == "|"):
            recurOne(numbers, row+1, col, visited, 3, dirs)
            recurOne(numbers, row-1, col, visited, 2, dirs)
        
        if(numbers[row][col] == "-" or numbers[row][col] == "."):
            recurOne(numbers, row, col + direction, visited, direction, dirs)
        
        if(numbers[row][col] == "/"):
            if(direction == -1):
                recurOne(numbers, row+1, col, visited, 3, dirs)
            if(direction == 1):
                recurOne(numbers, row-1, col, visited, 2, dirs)
        
        if(numbers[row][col] == "\\"):
            if(direction == -1):
                recurOne(numbers, row-1, col, visited, 2, dirs)
            if(direction == 1):
                recurOne(numbers, row+1, col, visited, 3, dirs)
        return
    direction =  -1 if direction == 2 else 1
    if(numbers[row][col] == "-"):
        recurOne(numbers, row, col-1, visited, -1, dirs)
        recurOne(numbers, row, col+1, visited, 1, dirs)
    
    if(numbers[row][col] == "|" or numbers[row][col] == "."):
        recurOne(numbers, row + direction, col, visited, 2 if direction == -1 else 3, dirs)
    
    if(numbers[row][col] == "/"):
        if(direction == -1):
            recurOne(numbers, row, col+1, visited, 1, dirs)
        if(direction == 1):
            recurOne(numbers, row, col-1, visited, -1, dirs)
    
    if(numbers[row][col] == "\\"):
        if(direction == -1):
            recurOne(numbers, row, col-1, visited, -1, dirs)
        if(direction == 1):
            recurOne(numbers, row, col+1, visited, 1, dirs)

def part2(numbers):
    """Solve part 2."""
    macks = -1
    #Left to Right
    for k in range(len(numbers)):
        visited = [[False for i in r] for r in numbers]
        recurOne(numbers, k, 0, visited, 1, [[set() for i in r] for r in numbers])
        macks = max(macks, sum([sum(r) for r in visited]))
    
    #Top to Down
    for k in range(len(numbers[0])):
        visited = [[False for i in r] for r in numbers]
        recurOne(numbers, 0, k, visited, 3, [[set() for i in r] for r in numbers])
        macks = max(macks, sum([sum(r) for r in visited]))
    
    #Down to Top
    for k in range(len(numbers[0])):
        visited = [[False for i in r] for r in numbers]
        recurOne(numbers, len(numbers)-1, k, visited, 2, [[set() for i in r] for r in numbers])
        macks = max(macks, sum([sum(r) for r in visited]))
    
    #Right to Left
    for k in range(len(numbers)):
        visited = [[False for i in r] for r in numbers]
        recurOne(numbers, k, len(numbers[0])-1, visited, -1, [[set() for i in r] for r in numbers])
        macks = max(macks, sum([sum(r) for r in visited]))

    
    return macks
    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(16)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))