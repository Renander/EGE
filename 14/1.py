#https://inf-ege.sdamgia.ru/problem?id=33186

def f(n):
    s=''
    while n>0:
        s = str(n % 7) + s
        n //= 7
    return s

k = 343**5 - 7**9 + 48
k2= f(k)
print(k2.count('6'))
