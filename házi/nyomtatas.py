def main():
    oldalak = "1-4,7,9,11-15"
    li = []

    for i in oldalak.split(","):
        if len(i) >= 3:
            old = i.split("-")

            elso = int(old[0])
            utolso = int(old[1]) + 1

            for n in range(elso, utolso):
                li.append(n)
        else:
            li.append(int(i))

    print(li)


if __name__ == "__main__":
    main()