

if __name__ == "__main__" :
    n = input()
    D = {1:0 , 2:0,3:0,4:0}
    a = list(map(int, input().split()))
    for i in D : D[i] +=1 ;
    res = D[4] + D[3] + D[2]//4 
    D[1] -= D[3]
    if D[2] %2==1 : res += 1; D[2]-=2
    if D[1] > 0 : res += (D[1] +3)//4;
    print (res)