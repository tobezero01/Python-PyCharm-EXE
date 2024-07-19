
def thap(n,A,B,C) :
    if n == 1 : print("chuyen dia %d tu %c sang %c" % (n,A,B))
    else :
        thap(n-1,A,C,B)
        print("chuyen dia %d tu %c sang %c" % (n,A,B))
        thap(n-1,C,B,A)


if __name__ == "__main__":
    thap(3,'A', 'B', 'C')