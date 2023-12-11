# aoc 2023 10.py

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
    for ind, i in enumerate(numbers):
        if i.find("S") > -1:
            return (recur(ind, i.find("S"), numbers, 1, [[False for char in i] for i in numbers]) - 1)/2
    print("EO1____________")

def recur(x, y, numbers, count, visited):
    if(visited[x][y]):
        if(numbers[x][y] == "S"):
            return count
        return -1
    visited[x][y] = True

    results = []

    canGoIfOnLeft = ["L", "F", "-", "S"]
    canGoIfOnDown = ["L", "J", "|", "S"]
    canGoIfOnRight = ["J", "7", "-", "S"]
    canGoIfOnUp = ["7", "F", "|", "S"]
    if(numbers[x][y] == "S"):
        if(numbers[x-1][y] in canGoIfOnUp):
            results.append(recur(x-1, y, numbers, count+1, visited))
        if(numbers[x+1][y] in canGoIfOnDown):
            results.append(recur(x+1, y, numbers, count+1, visited))
        if(numbers[x][y-1] in canGoIfOnLeft):
            results.append(recur(x, y-1, numbers, count+1, visited))
        if(numbers[x][y+1] in canGoIfOnRight):
            results.append(recur(x, y+1, numbers, count+1, visited))
    
    elif(numbers[x][y] == "|"):
        if numbers[x-1][y] in canGoIfOnUp:
            results.append(recur(x-1, y, numbers, count+1, visited))
        if numbers[x+1][y] in canGoIfOnDown:
            results.append(recur(x+1, y, numbers, count+1, visited))
        else:
            return -1
    elif(numbers[x][y] == "-"):
        if numbers[x][y+1] in canGoIfOnRight:
            results.append(recur(x, y+1, numbers, count+1, visited))
        if numbers[x][y-1] in canGoIfOnLeft:
            results.append(recur(x, y-1, numbers, count+1, visited))
        else:
            return -1
    elif(numbers[x][y] == "F"):
        if numbers[x+1][y] in canGoIfOnDown:
            results.append(recur(x+1, y, numbers, count+1, visited))
        if numbers[x][y+1] in canGoIfOnRight:    
            results.append(recur(x, y+1, numbers, count+1, visited))
        else:
            return -1
    elif(numbers[x][y] == "L"):
        if numbers[x-1][y] in canGoIfOnUp:
            results.append(recur(x-1, y, numbers, count+1, visited))
        if numbers[x][y+1] in canGoIfOnRight:
            results.append(recur(x, y+1, numbers, count+1, visited))
        else:
            return -1
    elif(numbers[x][y] == "J"):
        if numbers[x-1][y] in canGoIfOnUp:
            results.append(recur(x-1, y, numbers, count+1, visited))
        if numbers[x][y-1] in canGoIfOnLeft:
            results.append(recur(x, y-1, numbers, count+1, visited))
        else:
            return -1
    elif(numbers[x][y] == "7"):
        if numbers[x][y-1] in canGoIfOnLeft:
            results.append(recur(x, y - 1, numbers, count+1, visited))
        if numbers[x+1][y] in canGoIfOnDown:
            results.append(recur(x+1, y, numbers, count+1, visited))
        else:
            return -1
    return max(results)


def part2(numbers):
    """Solve part 2."""
    for ind, i in enumerate(numbers):
        if i.find("S") > -1:
            path = (recurCountingArea(ind, i.find("S"), numbers, 1, [[False for char in i] for i in numbers], []))[1]
            path += [path[0]]
            path = [list(i) for i in path]
            s = 0
            for ind, k in enumerate(path):
                if(numbers[k[0]][k[1]] == "L"):
                    path[ind] = (k[0]-1, k[1]+1)
                if(numbers[k[0]][k[1]] == "J"):
                    path[ind] = (k[0]-1, k[1]-1)
                if(numbers[k[0]][k[1]] == "F"):
                    path[ind] = (k[0]+1, k[1]+1)
                if(numbers[k[0]][k[1]] == "7"):
                    path[ind] = (k[0]+1, k[1]-1)
            for k in range(1, len(path)):
                s += (path[k][0]+path[k-1][0]) * (path[k][1]-path[k-1][1])
            return s//2
    print("EO1____________")

def recurCountingArea(x, y, numbers, count, visited, path):
    if(visited[x][y]):
        if(numbers[x][y] == "S"):
            return (count, path)
        return (-1, path)
    visited[x][y] = True

    results = []

    canGoIfOnLeft = ["L", "F", "-", "S"]
    canGoIfOnDown = ["L", "J", "|", "S"]
    canGoIfOnRight = ["J", "7", "-", "S"]
    canGoIfOnUp = ["7", "F", "|", "S"]
    if(numbers[x][y] != "|" and numbers[x][y] != "-"):
        path += [(x, y)]

    if(numbers[x][y] == "S"):
        if(numbers[x-1][y] in canGoIfOnUp):
            results.append(recurCountingArea(x-1, y, numbers, count+1, visited, path))
        if(numbers[x+1][y] in canGoIfOnDown):
            results.append(recurCountingArea(x+1, y, numbers, count+1, visited, path))
        if(numbers[x][y-1] in canGoIfOnLeft):
            results.append(recurCountingArea(x, y-1, numbers, count+1, visited, path))
        if(numbers[x][y+1] in canGoIfOnRight):
            results.append(recurCountingArea(x, y+1, numbers, count+1, visited, path))
    
    elif(numbers[x][y] == "|"):
        if numbers[x-1][y] in canGoIfOnUp:
            results.append(recurCountingArea(x-1, y, numbers, count+1, visited, path))
        if numbers[x+1][y] in canGoIfOnDown:
            results.append(recurCountingArea(x+1, y, numbers, count+1, visited, path))
        else:
            return (-1, path)
    elif(numbers[x][y] == "-"):
        if numbers[x][y+1] in canGoIfOnRight:
            results.append(recurCountingArea(x, y+1, numbers, count+1, visited, path))
        if numbers[x][y-1] in canGoIfOnLeft:
            results.append(recurCountingArea(x, y-1, numbers, count+1, visited, path))
        else:
            return (-1, path)
    elif(numbers[x][y] == "F"):
        if numbers[x+1][y] in canGoIfOnDown:
            results.append(recurCountingArea(x+1, y, numbers, count+1, visited, path))
        if numbers[x][y+1] in canGoIfOnRight:    
            results.append(recurCountingArea(x, y+1, numbers, count+1, visited, path))
        else:
            return (-1, path)
    elif(numbers[x][y] == "L"):
        if numbers[x-1][y] in canGoIfOnUp:
            results.append(recurCountingArea(x-1, y, numbers, count+1, visited, path))
        if numbers[x][y+1] in canGoIfOnRight:
            results.append(recurCountingArea(x, y+1, numbers, count+1, visited, path))
        else:
            return (-1, path)
    elif(numbers[x][y] == "J"):
        if numbers[x-1][y] in canGoIfOnUp:
            results.append(recurCountingArea(x-1, y, numbers, count+1, visited, path))
        if numbers[x][y-1] in canGoIfOnLeft:
            results.append(recurCountingArea(x, y-1, numbers, count+1, visited, path))
        else:
            return (-1, path)
    elif(numbers[x][y] == "7"):
        if numbers[x][y-1] in canGoIfOnLeft:
            results.append(recurCountingArea(x, y - 1, numbers, count+1, visited, path))
        if numbers[x+1][y] in canGoIfOnDown:
            results.append(recurCountingArea(x+1, y, numbers, count+1, visited, path))
        else:
            return (-1, path)
    if(numbers[x][y] != "|" and numbers[x][y] != "-"):
        path = path[0:-1]

    return max(results, key=lambda x : x)

if __name__ == "__main__":
    numbers = parse(10)
    print(part1(numbers))
    print(part2(numbers))