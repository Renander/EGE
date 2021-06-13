# https://inf-ege.sdamgia.ru/problem?id=9788

def F(x,y,z):
    return int((not(x)and y and z) or (not(x) and y and not(z)) or (not(x) and not(y) and not(z)))


p=[0,1]
for x in p:
    for y in p:
        for z in p:
            print(x,y,z,F(x,y,z))
