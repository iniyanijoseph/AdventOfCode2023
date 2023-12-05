# aoc 2023 5.py

import parse
import threading

def getinput(puzzle_input):
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
    seeds = list(map(int, numbers[0][numbers[0].find(":")+1:].split()))

    groups = []
    for line in numbers[1:]:
        if line == '':
            groups.append([])
        else:
            if(not ":" in line):
                groups[-1].append(list(map(int, line.split())))

    for ind, seed in enumerate(seeds):
        for group in groups:
            for line in group:
                if(line[1] <= seed < line[1] + line[2]):
                    seeds[ind] = line[0]+(seed-line[1])
                    seed = seeds[ind]
                    break
    
    return min(seeds)

    print("EO1____________")

def part2(numbers):
    """Solve part 2."""
    ranges = list(map(int, numbers[0][numbers[0].find(":")+1:].split()))
    
    ranges = list(zip(ranges, ranges[1:] + ranges[:1]))[::2]

    groups = []
    for line in numbers[1:]:
        if line == '':
            groups.append([])
        else:
            if(not ":" in line):
                groups[-1].append(list(map(int, line.split())))

    out = [2E31]*len(ranges)
    threads = []
    for ind, ele in enumerate(ranges):
        threads.append(threading.Thread(target=calcRange, args=(ele, groups, ind, out)))
    
    print(threads)

    for k in threads:
        k.start()
    
    for k in threads:
        k.join()
    
    return min(out)

    print("EO2____________")

def calcRange(ele, groups, i, out):
    s = 2E31
    for seed in range(ele[0], ele[0] + ele[1]):
        for group in groups:
            for line in group:
                if(line[1] <= seed < line[1] + line[2]):
                    seed = line[0]+(seed-line[1])
                    break
        k = min(seed, s)
        if(k != s):
            print(f"{s} --> {k}")
            s = k

    out[i] = s


if __name__ == "__main__":
    numbers = getinput(5)
    #print(numbers)
    #print(part1(numbers))
    print(part2(numbers))