p = [0 for _ in range(100000 + 1)]
for i in range(1, 100000 + 1):
    if i == 1:
        p[i] = 1
    if i - 1 >= 1:
        p[i] += p[i - 1]
    if i % 2 == 0 and i // 2 >= 1:
        p[i] += p[i//2]
    if i % 3 == 0 and i // 3 >= 1:
        p[i] += p[i//3]
    
    
print(p[100000])
