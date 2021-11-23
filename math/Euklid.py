#!/usr/bin/env python3

def Euklid(a,b):
    if(b == 0):
        return a
    tmp = b
    b = a % b
    a = tmp
    return Euklid(a,b)

def main():
    
    ggT = Euklid(128,36)
    print(ggT)

    ggT = Euklid(41,61)
    print(ggT)



if(__name__ == "__main__"):
    main()
