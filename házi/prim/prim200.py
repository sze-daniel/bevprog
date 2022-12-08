import def_prime as prim

def main():
    ossz = 0
    for i in range(1, 200):
        if prim.prime(i):
            ossz += i
    
    print(ossz)
            
if __name__ ==  "__main__":
    main()