from cmath import sqrt


def main():
    print("Pitagorasz-tétel:")
    a_h = int(input("A háromszög egyik befogója: "))
    b_h = int(input("A háromszög másik befogója: "))
    c_h = sqrt(pow(a_h, 2) + pow(b_h, 2))
    print("A háromszög átfogója: {0}".format(c_h))
    print()
    
    print("Téglalap területe, kerülete:")
    a_t = int(input("A téglalap egyik oldala (cm): "))
    b_t = int(input("A téglalap másik oldala (cm): "))
    ter = a_t * b_t
    ker = 2 * a_t + 2 *b_t
    print("A téglalap kerülete: {0}cm, területe: {1}cm^2.".format(ker, ter))
    print()
    
    print("Másodfokú egyenlet:")
    a_m = int(input("Az egyenlet első száma: "))
    b_m = int(input("Az egyenlet második száma: "))
    c_m = int(input("Az egyenlet harmadik száma: "))
    d = sqrt(pow(b_m, 2) - 4 * a_m * c_m)
    x1 = (-b_m + d) / 2 * a_m
    x2 = (b_m - d) / 2 * a_m
    print("Az egyenlet két gyöke: {0}, {1}.".format(x1, x2))
        
if __name__ == "__main__":
    main()