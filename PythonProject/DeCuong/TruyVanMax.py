class node: #elem = quan li doan [a,b)
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.elem=-int(10**9)
        if a+1==b: self.left,self.right=None,None
        else:
            self.left=node(a,(a+b)//2)
            self.right=node((a+b)//2,b)
def update(H,i,x): #update a[i]=x
    H.elem=max(H.elem,x)
    if H.left !=None: update(H.left if i<H.left.b else H.right,i,x)

def get(H,L,R):
    if H.a==L and H.b==R: return H.elem
    if R<=H.left.b: return get(H.left,L,R)
    if(L>=H.right.a): return get(H.right,L,R)
    return max(get(H.left,L,H.left.b),get(H.right,H.right.a,R))
if __name__ == '__main__':
    n,m=map(int,input().split())
    root = node(1,n+1)
    for i,x in enumerate(map(int,input().split()),1): update(root,i,x)
    for i in range(m):
        L,R=map(int,input().split())
        print(get(root,L,R+1))