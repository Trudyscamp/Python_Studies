n = int(input('termos: '))
p1 = 1
p2 = 1
if n ==1:
    s = str(p1)
else:
     s = str(p1)+", "+str(p2)
    for i in range(n-2):
        p = p1 + p2
        s=s+", "+str(p)
        p1 = p2
        p2 = p
print(s)            