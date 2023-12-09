# aoc 2023 _.py

import pathlib
import sys
import binascii

def parse(puzzle_input):
    """Parse input."""
    # Read each line as a string
    file = open(f'{puzzle_input}.txt',mode='r')
    inp = file.read().split("\n")
    file.close()

    inp = [line.split() for line in inp]

    # Convert each line to an integer 
    # inp = list(map(lambda x : int(x) if x != "" else -1, inp))
    
    return inp

def score(hand1):
    hand1 = hand1[0]
    freq1 = {i:hand1.count(i) for i in set(hand1)}

    score = 0

    numPairs = 0

    for k in freq1:
        if freq1[k] == 2:
            numPairs += 1 

    if(5 in freq1.values()):
        score += 60000000000
    elif 4 in freq1.values():
        score += 50000000000
    elif 3 in freq1.values() and 2 in freq1.values():
        score += 40000000000
    elif 3 in freq1.values():
        score += 30000000000
    elif(numPairs == 2):
        score += 20000000000
    elif numPairs == 1:
        score += 10000000000
    
    hand1 = hand1.replace("J", "B")
    hand1 = hand1.replace("Q", "C")
    hand1 = hand1.replace("K", "D")
    hand1 = hand1.replace("A", "E")
    hand1 = hand1.replace("T", "A")


    for ind, char in enumerate(hand1):
        if(char.isdigit()):
            score += 10**(2*(4-ind)) * int(char)
        else:
            score += 10**(2*(4-ind)) * (ord(char) - ord("A") + 10)

    return score

def part1(numbers):
    """Solve part 1."""
    numbers = sorted(numbers, key=score)
    return sum([(ind+1) * int(ele[1]) for ind, ele in enumerate(numbers)])

    print("EO1____________")

def rescore(hand1):
    hand1 = hand1[0]
    freq1 = {i:hand1.count(i) for i in set(hand1)}
    jfreq = freq1.pop('J', 0)

    score = 0

    vals = list(freq1.values())

    k = 0
    
    try:
        k = max(vals)
        vals.remove(k)
    except:
        pass
    vals.append(k+jfreq)

    numPairs = 0

    for k in freq1:
        if k == 2:
            numPairs += 1

    # Issue is case 55AJ8

    if(5 in vals):
        score += 60000000000
    elif 4 in vals:
        score += 50000000000
    elif 3 in vals and 2 in vals:
        score += 40000000000
    elif 3 in vals:
        score += 30000000000
    elif(numPairs == 2):
        score += 20000000000
    elif numPairs == 1:
        score += 10000000000
    
    hand1 = hand1.replace("J", "1")
    hand1 = hand1.replace("Q", "B")
    hand1 = hand1.replace("K", "C")
    hand1 = hand1.replace("A", "D")
    hand1 = hand1.replace("T", "A")


    for ind, char in enumerate(hand1):
        if(char.isdigit()):
            score += 10**(2*(4-ind)) * int(char)
        else:
            score += 10**(2*(4-ind)) * (ord(char) - ord("A") + 10)

    return score

def part2(numbers):
    """Solve part 2."""
    numbers = sorted(numbers, key=rescore)
    return sum([(ind+1) * int(ele[1]) for ind, ele in enumerate(numbers)])
    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(7)
    print(part1(numbers))
    print(part2(numbers))