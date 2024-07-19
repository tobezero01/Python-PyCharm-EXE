D = {}

def tachSau(a) :
    global D
    if a in D.keys() : return
    D[a] = True
    if len(a) > 1 :
        tachSau(a[1:]) 
        tachSau(a[:len(a)-1])
    
if __name__ == '__main__' :
    x=tachSau("banana")
    for x in D.keys() : print(x, sep = " ")