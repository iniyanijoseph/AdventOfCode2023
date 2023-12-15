# aoc 2023 15.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    # Read each line as a string
    file = open(f'{puzzle_input}.txt',mode='r')
    inp = file.read().split(",")
    file.close()

    # Convert each line to an integer 
    # inp = list(map(lambda x : int(x) if x != "" else -1, inp))
    
    return inp

def part1(numbers):
    """Solve part 1."""
    s = 0
    for i in numbers:
        cval = 0
        for j in i:
            cval += ord(j)
            cval *= 17
            cval %= 256
        s += cval

    return s
    print("EO1____________")

def part2(numbers):
    """Solve part 2."""
    boxes = {}
    for i in numbers:
        if "-" in i:
            code, _ = i.split("-")
            for k in boxes:
                for ind, r in enumerate(boxes[k]):
                    if r[0] == code: 
                        boxes[k].pop(ind)
                
        else:
            code, val = i.split("=")
            cval = 0
            for j in code:
                cval += ord(j)
                cval *= 17
                cval %= 256
            
            foundit = False
            if not cval in boxes:
                boxes[cval] = [(code, val)]
            else:
                for ind, r in enumerate(boxes[cval]):
                    if r[0] == code: 
                        boxes[cval][ind] = (code, val)
                        foundit = True
                if not foundit:
                    boxes[cval].append((code, val))


    s = 0

    for k in boxes:
        for ind, r in enumerate(boxes[k]):
            s += (k+1)*(ind+1)*int(r[1])

    return s
    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(15)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))