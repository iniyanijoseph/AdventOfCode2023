# aoc 2023 1.py

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
    s = 0
    for k in numbers:
        l = ""
        for j in k:
            if(j.isdigit()):
                l += j
        if(len(l) == 1):
            l = 2*l
        if(len(l) > 2):
            l = l[0] + l[-1]
        s += int(l)
    return s
    print("EO1____________")

def part2(numbers):
    """Solve part 2."""
    s = 0
    numr = {"on":1, "tw":2, "th":3, "fo":4, "fi":5, "si":6, "se":7, "ei":8, "ni":9}

    for i, ele in enumerate(numbers):
        rsetin = [ele.find("one"),ele.find("two"),ele.find("three"),ele.find("four"),ele.find("five"),ele.find("six"),ele.find("seven"),ele.find("eight"),ele.find("nine"), ele.find("1"), ele.find("2"), ele.find("3"), ele.find("4"), ele.find("5"), ele.find("6"), ele.find("7"), ele.find("8"), ele.find("9")]
        k = sorted(list(filter(lambda x: x != -1, rsetin)))
        t = ""
        if(ele[k[0]].isdigit()):
            t += str(ele[k[0]])
        else:
            t += str(numr[ele[k[0]:k[0]+2]])
        
        rsetin = [ele.rfind("one"),ele.rfind("two"),ele.rfind("three"),ele.rfind("four"),ele.rfind("five"),ele.rfind("six"),ele.rfind("seven"),ele.rfind("eight"),ele.rfind("nine"), ele.rfind("1"), ele.rfind("2"), ele.rfind("3"), ele.rfind("4"), ele.rfind("5"), ele.rfind("6"), ele.rfind("7"), ele.rfind("8"), ele.rfind("9")]
        k = sorted(list(filter(lambda x: x != -1, rsetin)))

        if(ele[k[-1]].isdigit()):
            t += str(ele[k[-1]])
        else:
            t += str(numr[ele[k[-1]:k[-1]+2]])
        
        s += int(t)

    return s
    print("EO2____________")


if __name__ == "__main__":
    numbers = parse(1)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))