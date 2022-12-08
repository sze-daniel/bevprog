def main():
    with open('pi_vers.txt', 'r') as f, open('pi.txt', 'w') as pi:
        li = [len(i) for i in f.read().split(' ')]

        print(li[0], file=pi)

if __name__ == "__main__":
    main()