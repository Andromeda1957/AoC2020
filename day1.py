def main():
    with open('day1.txt', 'r') as f:
        data = f.read().split()
        data = [eval(i) for i in data]

        for tgt in data:
            for nums in data:
                for a in data:
                    if tgt + nums + a == 2020:
                        print(tgt, nums, a)
                        print(tgt * nums * a)

if __name__ == '__main__':
    main()