def main():
    x = input("Adjon meg egy számot: ")
    if x == "".join(reversed(x)):
        print("{0} egy tükörszám.".format(x))
    else:
        print("{0} nem tükörszám.".format(x))

if __name__ == "__main__":
    main()