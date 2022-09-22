def main():
    natrium = int(input("Natrium: "))
    klor = int(input("Klor: "))
    nacl = 0
    exNa = 0
    exCl = 0
    
    if klor * 2 == natrium:
        nacl = natrium
    elif klor *2 < natrium:
        nacl = klor *2
        exNa = natrium - (klor * 2)
    else:
        nacl = natrium
        exCl = klor * 2 -natrium
    print("Létrjött só: {0}, maradék nátriumatom: {1}, maradék klóratom: {2}.".format(nacl, exNa, exCl))
               

if __name__=="__main__":
    main()