def main():
    with open('string1.py', 'r') as a, open('string1_clean.py', 'w') as b:
        lines = a.readlines()

        [print(l, file=b)
         for l in lines if not l.startswith("#") if l.rstrip()]


if __name__ == "__main__":
    main()