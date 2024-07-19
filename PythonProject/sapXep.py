from functools import cmp_to_key
from collections import namedtuple
import collections
def cmp(a,b) :
    if a%3<b%3 : return 1
    if a%3>b%3 : return -1
    
    return a - b

if __name__ == "__main__" :
    a = [323, 32, 42, 5, 6, 47, 11, 12]
    b =sorted(a, key=cmp_to_key(cmp))
    print(b)
    
    print("----------------------------------------------------------------")
    point = namedtuple("diem", "x y")
    a = point(3,4)
    print(a.x, a.y)
    print(a)
    
    D = collections.Counter(a)
    print(D)
    
    