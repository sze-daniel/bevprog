import random

def main():
    print("I thought of a number between 1 and 100.")
    x = 0
    n = random.randint(0,100)
    tipp = int(input("your guess> "))
    while n != tipp:
        if tipp > n:
            tipp = int(input("my number is smaller\nyour guess>"))
            x += 1
        elif tipp < n:
            tipp = int(input("my number is larger\nyour guess>"))
            x += 1

    print(f"Good job! That's it!\nNumber of guesses: {x}")

if __name__ == "__main__":
    main()