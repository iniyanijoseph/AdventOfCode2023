# aoc 2023 19.py

import re

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
    workflows = numbers[0].split("\n")
    part = numbers[1].split("\n")

    flows = [re.split('{|}|,',line) for line in workflows]
    
    keys = {}
    
    for line in flows:
        key = line[0]
        order = []
        for ele in line[1:-2]:
            k, sign, value, target = (re.split('<|>', ele.split(":")[0])[0], -1 if '<' in ele else 1, re.split('<|>', ele.split(":")[0])[1], ele.split(":")[1])
            order.append([k, sign, int(value), target]) 

        default = line[-2]

        order.append(['', -1, 10**10, default])

        keys[key] = order    

    part = [[r for r in re.split('{|}|,', line) if r != ""] for line in part]
    prt = []
    for k in part:
        temp = {}
        for r in k:
            temp[r.split("=")[0]] = int(r.split("=")[1])
        prt.append(temp)

    s = 0
    for task in prt:
        current = "in"
        while(1):
            for k in keys[current] if not current in ["A", "R"] else []:
                key, sign, value, target = k
                if key != '':
                    v = task[key]
                    if (v*sign > value * sign):
                        current = target
                        break
                else:
                    current = target
                    break
            if(current == "A"):
                s += sum(task.values())
                break
            if(current == "R"):
                break
    return s
    print("EO1____________")

def part2(numbers):
    """Solve part 2."""
    print("EO2____________")

if __name__ == "__main__":
    numbers = parse(19)
    print(numbers)
    print(part1(numbers))
    print(part2(numbers))