# aoc 2023 18.py

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
    numbers = [number.split(" ") for number in numbers]
    coord = [0, 0]
    perimeter = 0
    points = []
    for row in numbers:
        xskew = 1 if row[0] == "R" else -1 if row[0] == "L" else 0
        yskew = 1 if row[0] == "U" else -1 if row[0] == "D" else 0

        x,y = coord 
        points.append([x,y])
        coord[0] += xskew * int(row[1])
        coord[1] += yskew * int(row[1])

        perimeter += abs(xskew * int(row[1])) + abs(yskew * int(row[1]))

    points.append([0, 0])

    area = 0
    for i in range(1, len(points)):
        area += 0.5*(points[i][0]-points[i-1][0]) *  (points[i][1]+points[i-1][1]) 

    return abs(area) + perimeter//2 + 1

    print("EO1____________")

def part2(numbers):
    """Solve part 2."""
    numbers = [number.split(" ") for number in numbers]
    coord = [0, 0]
    perimeter = 0
    points = []
    for row in numbers:
        l = (row[2])[2:-2]
        r = int((row[2])[-2])

        xskew = 1 if r == 0 else -1 if r == 2 else 0
        yskew = 1 if r == 3 else -1 if r == 1 else 0

        x,y = coord
        points.append([x,y])
        hexInt = int(l, 16)
        coord[0] += xskew * hexInt
        coord[1] += yskew * hexInt

        print(xskew, yskew, hexInt)

        perimeter += abs(xskew * hexInt) + abs(yskew * hexInt)

    points.append([0, 0])

    area = 0
    for i in range(1, len(points)):
        area += 0.5*(points[i][0]-points[i-1][0]) *  (points[i][1]+points[i-1][1]) 


    return int(abs(area) + perimeter//2 + 1)

    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(18)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))