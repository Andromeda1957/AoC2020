#!/usr/bin/python3
import re

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

def part_two(data, fields):
    invalid = False
    pattern = re.compile('[0-9a-fA-f]+')
    ecl = ['amb', 'blu', 'brn', 'gry', 'hzl', 'oth', 'grn']
    invalid_list = []
    valid = len(data)
    
    for line in data:
        split_fields = line.split()
        
        for split_field in split_fields:
            if split_field[:3] not in fields:
                if line not in invalid_list:
                    invalid_list.append(line)
                    valid -= 1
            elif split_field[:3] == 'byr':
                if int(split_field[4:]) < 1920 or int(split_field[4:]) > 2020 or int(split_field[4:]) < 1000:
                    if line not in invalid_list:
                        invalid_list.append(line)
                        valid -= 1

            elif split_field[:3] == 'iyr':
                if int(split_field[4:]) < 2010 or int(split_field[4:]) > 2020 or int(split_field[4:]) < 1000:
                    if line not in invalid_list:
                        invalid_list.append(line)
                        valid -= 1

            elif split_field[:3] == 'eyr':
                if int(split_field[4:]) < 2020 or int(split_field[4:]) > 2030 or int(split_field[4:]) < 1000:
                    if line not in invalid_list:
                        invalid_list.append(line)
                        valid -= 1

            elif split_field[:3] == 'hgt':
                try:
                    if split_field[-2:] == 'cm':
                        if int(split_field[4:7]) < 150 or int(split_field[4:7]) > 193:
                            if line not in invalid_list:
                                invalid_list.append(line)
                                valid -= 1

                    elif split_field[-2:] == 'in':
                        if int(split_field[4:7]) < 59 or int(split_field[4:7]) > 76:
                            if line not in invalid_list:
                                invalid_list.append(line)
                                valid -= 1

                except ValueError:
                    if line not in invalid_list:
                        invalid_list.append(line)
                        valid -= 1
            
            elif split_field[:3] == 'pid':
                if len(split_field[4:]) != 9 or split_field[4:].isnumeric() == False:
                    if line not in invalid_list:
                        invalid_list.append(line)
                        valid -= 1

            elif split_field[:3] == 'ecl':
                a = 0
                for e in ecl:
                    if split_field[4:] == e:
                        a += 1
                if a != 1:
                    if line not in invalid_list:
                        split_field[4:]
                        invalid_list.append(line)
                        valid -= 1

            elif split_field[:3] == 'hcl':
                chars = 'abcdef0123456789'

                for char in split_field[6:]:
                    if char not in chars:
                        if line not in invalid_list:
                            invalid_list.append(line)
                            valid -= 1

                if split_field[4:5] != '#':
                    if line not in invalid_list:
                        invalid_list.append(line)
                        valid -= 1
                    break
                if pattern.fullmatch(split_field[6:]) is None or len(split_field[6:]) != 5:
                    if line not in invalid_list:
                        invalid_list.append(line)
                        valid -= 1

    for inv in invalid_list:
        print(inv, '\n\n')


    print(len(invalid_list))
    return valid

def main():
    data = read_file()
    fields = ['hcl', 'ecl', 'hgt', 'byr', 'pid', 'eyr', 'iyr']
    fields1 = ['hcl', 'ecl', 'hgt', 'byr', 'pid', 'eyr', 'iyr', 'cid']
    part1 = part_one(data, fields)
    part2 = part_two(data, fields1)
    print(f'Part1: {part1}')
    print(f'Part2: {part2}')
        

if __name__ == '__main__':
    main()
