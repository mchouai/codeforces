def f(ch):
    r=ch[-1]
    for i in range(len(ch)-1):
        if ch[i]!=ch[i+1]:
            r=ch[i]+r


    return r


t=int(input())
ch=input()
k=len(f(ch))
print(t-k)

