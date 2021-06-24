p=[0 for i in range (1000)]
for i in range(2,30 + 1):
    if i ==2 :
        p[i] = 1
    if i - 2 >= 2:
        p[i] += p[i - 2]
    if i % 5 ==0 and i//5 >=2:
        p[i] += p[i//5]

for i in range(31,50 + 1):
    if i == 25:
        continue
    if i - 2 >= 25:
        p[i] += p[i - 2]
    if i % 5 ==0 and i//5 >=25:
        p[i] += p[i//5]
print(p[30])
