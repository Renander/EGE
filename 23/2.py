#https://inf-ege.sdamgia.ru/problem?id=3607

p=[0 for i in range (1000)]
for i in range(2,50 + 1):
    if i ==2 :
        p[i] = 1
    if i - 2 >= 2:
        p[i] += p[i - 2]
    if i % 5 ==0 and i//5 >=2:
        p[i] += p[i//5]
print(p[50])
