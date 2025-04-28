def negacja(x):
    wynik=''
    for i in range(len(x)):
        if x[i]=='0':
            wynik+='1'
        else:
            wynik+='0'
    return wynik

def transformacja(S,k):
    if k==0:
        return S
    else:
        T=transformacja(S,k-1)
        N=negacja(T)
    return T+N

from collections import Counter
print(transformacja('0',4))

cyfra=transformacja('0',4)

print(Counter(cyfra))
print(sum(Counter(cyfra).values()))

taba=[]
for i in range(len(cyfra)-4):
    print(cyfra[i:i+4])
    taba.append(cyfra[i:i+4])


print(Counter(taba))