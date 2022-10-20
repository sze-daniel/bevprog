def csere(szavak, szo1, szo2):
    s = szavak.split(" ")
    szo1 = s[1]
    szo2 = s[0]
    print("{0} {1}".format(szo1,szo2))

def main():
    szo1=input("Adjon meg egy szót: ")
    szo2=input("Adjon meg egy szót, ami az előző elé kerül: ")
    szavak = szo1 + " " + szo2
    csere(szavak, szo1, szo2)

if __name__ == "__main__":
    main()