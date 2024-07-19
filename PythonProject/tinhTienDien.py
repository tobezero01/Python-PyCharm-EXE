import math
n = input()
n = int(n)
if n < 100 :  t = n
elif n <= 250 : t= 100 + (n-100)*1.2
elif n <= 500 : t= 100 + 150*1.2 + (n- 250)*1.7
else : t = 100 + 150*1.2 + 250*1.7 + (n-500)*2.2 
print(t)


if __name__ == "__main__" :
    n = int(input())
    a = [100,250,500]
    b = [1,1.2,1.7,2.2] 
    s = 0
    for u,v in zip(a[::-1],b[::-1]) :
        