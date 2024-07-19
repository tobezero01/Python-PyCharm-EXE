n = int(input())
voBia = n//28
res = voBia
while voBia >= 3 :
    temp = voBia // 3
    res += temp
    voBia = temp + voBia%3
print(res)