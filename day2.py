#!/usr/bin/python3

def get_policy(data):
    counter = 0
    policy = []
    max = len(data)

    while counter < max:
            policy.append(data[counter])
            counter = counter + 3

    return policy

def get_letter(data):
    counter = 1
    letter = []
    new_letter = []
    max = len(data)

    while counter < max:
            letter.append(data[counter])
            counter = counter + 3

    for element in letter:
        element = element[:-1]
        new_letter.append(element)

    return new_letter

def get_password(data):
    counter = 2
    password = []
    max = len(data)

    while counter < max:
            password.append(data[counter])
            counter = counter + 3
            
    return password

def main():
    counter = 0
    counter1 = 0

    with open('day2.txt', 'r') as f:
        data = f.read().split()
        policy = get_policy(data)
        letter = get_letter(data)
        password = get_password(data)

        for num in range(len(policy)):
            policy_range = policy[num].split('-')
            policy_range = [eval(i) for i in policy_range]
            min = policy_range[0]
            max = policy_range[1]
            letter_counter = 0

            if letter[num] in password[num]:
                characters = [*password[num]]

                try:
                    if letter[num] == characters[min - 1] or letter[num] == characters[max - 1]:
                        if characters[min - 1] != characters[max - 1]:
                            counter1 = counter1 + 1
                except IndexError:
                    pass
            
                for element in characters:
                    if letter[num] == element:
                        letter_counter = letter_counter + 1
            
            if letter_counter >= min and letter_counter <= max:
                counter = counter + 1

    print(f'Part1: {counter}')
    print(f'Part2: {counter1}')

if __name__ == '__main__':
    main()