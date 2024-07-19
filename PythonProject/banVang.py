# bai toan ban vang

if __name__ == "__main__" :
    n = int(input())
    M,*a = list(map(int, input().split()))[::-1]
    s = 0
    for x in a :
        if M < x : M = x
        else : s += M-x
        
    print (s)