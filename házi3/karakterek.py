def valid(text, chars):
    
    for i in text:
        for j in chars:
            if i == j:
                print(j)
    
def main():
    text = input("Írjon be egy szöveget: ")
    chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    valid(text, chars)

if __name__ == "__main__":
    main()