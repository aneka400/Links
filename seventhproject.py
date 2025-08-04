# https://github.com/aneka400/Links.git
a = int(input())
b = []
for i in range(a):
    c = int(input())
    b.append(c)  
d = set(b)

a2 = int(input())
b2 = []
for i in range(a2):
    c2 = int(input())
    b2.append(c2)
d2 = set(b2)

print(d.union(d2))

tn = int(input())
btr = []
for i in range(tn):
    gh = int(input())
    btr.append(gh) 
df = set(btr)
tn2 = int(input())
btr2 = [] 
for i in range(tn2):
    gh2 = int(input())
    btr2.append(gh2)
df2 = set(b2)
print(df.intersection(df2))

n = int(input())
nuu = set()
for i in range(n):
    a = int(input())
    
    if a in nuu:
        print("Yes")
    else:
        print("No")
        nuu.add(a)
