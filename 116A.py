X = lambda : map(int,input().split())
t,=X()
tram=0
tramo=[]
for i in range(t):
    s,e = X()
    tram = tram-s+e
    tramo.append(tram)

print(max(tramo))