
if __name__ == "__main__" :
    D = {1:2, 'a' : 5,"ha noi" : "troi mat, "} 
    print(D[1])
    print(D['a'])
    x = input()
    if x in D.keys() : print(x)
    else : print("khong co phan tu can tim")