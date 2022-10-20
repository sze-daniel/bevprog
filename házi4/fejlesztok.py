class fejlesztok:
    def __init__(self, nev, fizetes, rang = "Junior", ev = 0):
        self.nev = nev
        self.fizetes = fizetes
        self.rang = rang
        self.ev = ev
        
    def femeles(self, emeles = 10000):
        self.fizetes += emeles
    
    def evek(self):
        self.ev += 1
        
    def rangok(self):
        if self.ev == 0:
            self.rang = "Intern"
        elif self.ev < 3:
            self.rang = "Junior"
        elif self.ev < 6:
            self.rang = "Medior"
        elif self.ev > 5:
            self.rang = "Senior"

def main():
    a = fejlesztok("Nev", 10000)
    
    print("Név: {0}; Rang: {1}; Bedolgozott évek: {2}; Fizetés: {3};".format(a.nev,a.rang,a.ev,a.fizetes))
   
if __name__ == "__main__":
    main()