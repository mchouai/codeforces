ch=input()
h="hello"
t=len(ch)
for i in range(t):
    if ch[i] == h[0]:
        h=h.replace(ch[0],'')

if h=="hello":
    print("YES")
else:
    print("NO")