from re import I


def main():
    n = int(input("A Fibonacci sorozat hányadik eleme?: "))
    i = 0
    a = 1
    b = 1
    while i < n:
        x = a + b
        a = b
        b = x
        i += 1
    print(a)
    

if __name__ == "__main__":
    main()