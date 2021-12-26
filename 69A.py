X = lambda : map(int , input().split())
t,=X()
L=[0,0,0]
for i in range(t):
    a,b,c=X()
    L[0]+=a
    L[1]+=b
    L[2]+=c
if L[0]==0 and L[1]==0 and L[2]==0:
    print("YES")
else:
    print("NO")

