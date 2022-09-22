def main():
    kor= int(input("Adja meg az élletkorát: "))
    
    if kor >= 21:
        print("Fogyaszthat Amerikában alkoholt.")
    elif kor >= 18:
        print("Vásárolhat dohányterméket Magyarországon.")
    elif kor >= 16:
        print("Szerezhet jogosítványt.")
    elif kor >= 12:
        print("Megnézheti egyedül a Shrek 2-t.")

if __name__=="__main__":
    main()