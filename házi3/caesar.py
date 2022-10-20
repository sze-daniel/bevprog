def main():
    kod = "kwwsv=22|rxwx1eh2gTz7z<Zj[fT"
    dekod = 3
    megfejt=""
    for i in range(len(kod)):
        x = kod[i]
        megfejt = megfejt + chr(ord(x)-dekod)
    print("A megfejtés: \n {0}".format(megfejt))

if __name__ == "__main__":
    main()