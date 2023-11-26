#!/usr/bin/python3

def read_file():
    with open('day3.txt', 'r') as f:
        data = f.read().split()

    return data

def list_lines(data):
    seperate_lines = []

    for line in data:
        seperate_lines.append([*line])
    
    return seperate_lines

def get_slope(x, y):
    counter = 0
    row = 0
    slope = 0
    data = read_file()
    lines = list_lines(data)

    while row + 1 < len(lines):
        counter += x
        row += y

        if lines[row][counter % len(lines[row])] == '#':
            slope += 1

    return slope

def main():    
    slope1 = get_slope(3, 1)
    slope2 = get_slope(1, 1)
    slope3 = get_slope(5, 1)
    slope4 = get_slope(7, 1)
    slope5 = get_slope(1, 2)
    part1 = slope1
    part2 = slope1 * slope2 * slope3 * slope4 * slope5
    print(f'Part1: {part1}')
    print(f'Part2: {part2}')

if __name__ == '__main__':
    main()