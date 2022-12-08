def main():
    li = [2, 4, 8, 3, 9, 7, 1]
    ossz = 0
    i = 0
    while i < len(li) -1:
        if li[i] > li[i+1]:
            ossz += (li[i] - li[i+1])
            i += 1
        elif li[i] < li[i+1]:
            ossz += (li[i+1] - li[i])
            i +=1
                
    print(ossz)

if __name__ == "__main__":
    main()