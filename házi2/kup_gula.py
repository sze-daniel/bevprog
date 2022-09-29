import math

def gula():
    print("Adja meg a gúla alapjának éleit: ")
    a = float(input("A téglalap a oldalda: "))
    b = float(input("A téglalap b oldalda: "))
    tter = a * b
    gm = float(input("Adja meg a gúla magasságát:" ))
    gt = tter * gm / 3
    print("A gúla térfogat: {0}.".format(gt))

def kup():
    r = float(input("Adja meg az alapkör sugarát: "))
    km = float(input("Adja meg a kúp magasságát: "))
    kt = pow(r, 2) * math.pi * km / 3
    print("A kúp térfogata: {0}.".format(kt))

def main():
    test = input("Gúla vagy kúp térfogatát szeretné kiszámítani?: ")
    if test == "kúp":
        kup()
    elif test == "gúla":
        gula()
    else:
        print("Nem megfelelő a megadott test.")

if __name__ == "__main__":
    main()