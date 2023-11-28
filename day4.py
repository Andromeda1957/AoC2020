#!/usr/bin/python3

def read_file():
    with open('day4.txt', 'r') as f:
        data = f.read().split("\n\n")

    return data

def part_one(data, fields):
    valid_passports = len(data)
    invalid_passports = 0

    for passport in data:
        for field in fields:
            if field not in passport:
                invalid_passports += 1
                break

    return valid_passports - invalid_passports

def remove_invalid(data, field):
    for passport in data:
        if field not in passport:
            data.remove(passport)

    return data

def part_two(data, fields):
    valid_passports = len(data)
    invalid_passports = 0
    
    for field in fields:
        passport_list = remove_invalid(data, field)

    for field in fields:
        passport_list = remove_invalid(data, field)
        
    

    print(len(data))

    return None

def main():

    data = read_file()
    fields = ['hcl', 'ecl', 'hgt', 'byr', 'pid', 'eyr', 'iyr']
    part1 = part_one(data, fields)
    part2 = part_two(data, fields)
    print(f'Part1: {part1}')
    print(f'Part2: {part2}')
        

if __name__ == '__main__':
    main()
