s="1A0B0C1"
l=list(s)
for i in range (1,len(l)-1):
    if l[i]=='A':
        r=int(l[i-1])&int(l[i+1])
    if l[i]=='B':
        r=int(l[i-1])|int(l[i+1])
    if l[i]=='C':
        r=int(l[i-1])^int(l[i+1])

print(r)
