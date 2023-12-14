# aoc 2023 _.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    # Read each line as a string
    file = open(f'{puzzle_input}.txt',mode='r')
    inp = file.read().split("\n\n")
    file.close()

    # Convert each line to an integer 
    # inp = list(map(lambda x : int(x) if x != "" else -1, inp))
    
    return inp

def part1(numbers):
    """Solve part 1."""
    horz = 0
    vert = 0

    for k in numbers:
        group = k.split("\n")
        for i in range(len(group)):
            offset = 0

            symmetric = True
            while i-offset >= 0 and i + offset + 1 < len(group):
                up = group[i-offset]
                down = group[i+offset+1]
                if(up != down):
                    symmetric = False
                    break
                offset+=1
        
            if(symmetric):
                if(i != len(group) -1):
                    horz += i + 1
                break
        group =[[row[i] for row in group] for i in range(len(group[0]))]
        for i in range(len(group)):
            offset = 0

            symmetric = True
            while i-offset >= 0 and i + offset + 1 < len(group):
                up = group[i-offset]
                down = group[i+offset+1]
                if(up != down):
                    symmetric = False
                    break
                offset+=1
        
            if(symmetric):
                if(i != len(group) -1):
                    vert += i + 1
                break
                
    horz *= 100


    return horz + vert
    print("EO1____________")

def part2(numbers):
    """Solve part 2."""
    horz = 0
    vert = 0

    for k in numbers:
        group = k.split("\n")
        #group =[[row[i] for row in group] for i in range(len(group[0]))]
        for i in range(len(group)):
            adHorz = 0
            offset = 0

            symmetric = True
            ndif = 0
            while i-offset >= 0 and i + offset + 1 < len(group):
                up = group[i-offset]
                print(i-offset, i+offset+1)
                down = group[i+offset+1]
                ndif = sum([up[j] != down[j] for j in range(len(up))])
                if(ndif > 1):
                    symmetric = False
                    break
                offset+=1
        
            if ndif == 0:
                symmetric = False

            if(symmetric):
                if(i != len(group) -1):
                    adHorz += i + 1
                break

        group =[[row[i] for row in group] for i in range(len(group[0]))]
        
        if adHorz == 0:
            for i in range(len(group)):

                offset = 0

                symmetric = True
                ndif = 0
                while i-offset >= 0 and i + offset + 1 < len(group):
                    up = group[i-offset]
                    print("col", i-offset, i+offset+1)
                    down = group[i+offset+1]
                    ndif = sum([up[j] != down[j] for j in range(len(up))])
                    if(ndif > 1):
                        symmetric = False
                        break
                    offset+=1
            
                if ndif == 0:
                    symmetric = False

                if(symmetric):
                    if(i != len(group) -1):
                        vert += i + 1
                    break
        else:
            horz += adHorz
        print()
    horz *= 100


    return horz + vert
    print("EO2____________")


if __name__ == "__main__":
    numbers = parse(13)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))