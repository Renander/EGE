# https://inf-ege.sdamgia.ru/problem?id=9206
p=[0 for i in range(1000)]
for i in range(2,10+1):
    if i == 2:
        p[i]=1
    if i-1>=2:
        p[i] += p[i-1]
    if i-3>=2:
        p[i] += p[i-3]
    if ((i+1)//2)>=2 and i%2!=0:
        p[i] += p[((i+1)//2)]

print(p[10])
