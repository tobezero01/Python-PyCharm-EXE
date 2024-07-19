a, b, c = list(map(int, input().split()))
m = int(input())
res = 0

while m > 0:
    i = m // 3
    if i > c:
        m -= 3 * c
        res += c
    else:
        m -= 3 * i
        res += i
        h = m // 2
        if h > b:
            m -= 2 * b
            res += b
        else:
            m -= 2 * h
            res += h + m
if m > 0:
    print("KHONG DOI DUOC")
else:
    print(res)
