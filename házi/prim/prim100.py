import def_prime as prim

def main():
    for i in range(1, 100):
        if prim.prime(i):
            print(i)
            
if __name__ ==  "__main__":
    main()