from math import *

if __name__ == "__main__" :
    a = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17	]
    b = "asadasadasadasad"
    c = (1,34,4,34,34,3,34)
    for i in a : print(i,end = " ")
    for i in b : print(i,end = " ")
    for i in c : print(i,end = " ")
    
    d = {2 : "a", 3 : "b", 4 : "c", 5 : "d"}
    print()
    print(d[2])
    for i in d.keys() : print(i,d[i])

    print("-----------------------------------------------------------------------------")
    
    b_1 = [x for x in a if x% 2 == 0]
    print(b_1)
    print (sum([i for i in a if i %3 == 0]))
    print (len([i for i in a if i %3 == 0]))
    print ("-----------------------------------------------------------------------------")
    for i,x in enumerate(a) : print(i , x)
    
    print ("-----------------------------------------------------------------------------")
    e = [0]*2
    f = 4*[2]
    g = 3*[4*[0]]
    g[0][0] = 2
    print(e)
    print(g)
    print ("-----------------------------------------------------------------------------")
    
    print ("Nhap Ma tran")
    n,m = map(int,input().split())
    
    a_2 = []
    for _ in range(n) :
        b_2 = list(map(int,input().split()))
        a_2.append(b_2)
    for x in a_2 : print(*x)
    print()
    
    print("xoay 90 do")
    b_2 = list(zip(*a[::-1]))
    print(b_2)
    for x in b_2 : print(*x)
    
    #print("xoay 180")
    
    print("----------------------------------------------------------------")
    
