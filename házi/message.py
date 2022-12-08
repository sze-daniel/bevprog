def main():
    text="""
    Cbcq Dgyk!
    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!
    Aqmimjjyi:
    Ynyb"""
    megfejtes=""""""
    for i in range(0, len(text)): #10 #: = 58
        if ord(text[i])+2 > 90 and ord(text[i])<97:
            megfejtes=megfejtes+chr(ord(text[i])-24)
        elif ord(text[i])>63 and ord(text[i])+2<=122:
           megfejtes=megfejtes+chr(ord(text[i])+2)
        elif ord(text[i])+2>122:
            megfejtes=megfejtes+chr(ord(text[i])-24)
        else:
            megfejtes=megfejtes+text[i]
            
    print(megfejtes)
        
    
if __name__=="__main__":
    main()