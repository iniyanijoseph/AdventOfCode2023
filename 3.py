# aoc 2023 3.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    # Read each line as a string
    file = open(f'{puzzle_input}.txt',mode='r')
    inp = file.read().split("\n")
    file.close()

    inp = [list(line) for line in inp]
    inp = [["."] + line + ["."] for line in inp]
    # Convert each line to an integer 
    # inp = list(map(lambda x : int(x) if x != "" else -1, inp))
    
    return inp

def part1(numbers):
    checked = [[False for ele in line] for line in numbers]
    lis = []
    """Solve part 1."""
    for i, line in enumerate(numbers):
        for j, element in enumerate(line):
            if(not element.isdigit() and element != "."):
                try:
                    order = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1)]
                    for l, k in order:
                        l = i + l
                        k = j + k
                        if(numbers[l][k].isdigit() and not checked[l][k]):
                            leftCounter = k
                            rightCounter = k + 1

                            leftBound = ""
                            rightBound = ""
                            while(numbers[l][leftCounter].isdigit()):
                                if(checked[l][leftCounter]):
                                    leftBound = ""
                                    break
                                leftBound += numbers[l][leftCounter]
                                checked[l][leftCounter] = True
                                leftCounter -=1 
                            leftBound = leftBound[::-1]

                            while(numbers[l][rightCounter].isdigit()):
                                if(checked[l][rightCounter]):
                                    rightBound = ""
                                rightBound += numbers[l][rightCounter]
                                checked[l][rightCounter] = True
                                rightCounter += 1 
                            
                            lis += [int(leftBound + rightBound)]

                except:
                    pass
    return sum(lis)
    print("EO1____________")

def part2(numbers):
    """Solve part 2."""
    checked = [[False for ele in line] for line in numbers]
    s = 0
    for i, line in enumerate(numbers):
        for j, element in enumerate(line):
            if(element == "*"):
                collected = []
                try:
                    order = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1)]
                    for l, k in order:
                        l = i + l
                        k = j + k
                        if(numbers[l][k].isdigit() and not checked[l][k]):
                            leftCounter = k
                            rightCounter = k + 1

                            leftBound = ""
                            rightBound = ""
                            while(numbers[l][leftCounter].isdigit()):
                                if(checked[l][leftCounter]):
                                    leftBound = ""
                                    break
                                leftBound += numbers[l][leftCounter]
                                checked[l][leftCounter] = True
                                leftCounter -=1 
                            leftBound = leftBound[::-1]

                            while(numbers[l][rightCounter].isdigit()):
                                if(checked[l][rightCounter]):
                                    rightBound = ""
                                rightBound += numbers[l][rightCounter]
                                checked[l][rightCounter] = True
                                rightCounter += 1 
                            
                            collected += [int(leftBound + rightBound)]
                except:
                    pass

                if(len(collected) == 2):
                    s += collected[0] * collected[1]
    return s
    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(3)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))