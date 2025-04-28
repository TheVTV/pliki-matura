# S - prefiks
#k kroki
#do ciagu obecnego dopisuje sie negacje ciagu
#0110100110010110

#101010

#101010010101

#101010010101 + 0101011010101


#101010|010101|010101101010

#0110100110010110

#01101001

#0110100110010110

def transform(litera,k):
    while k > 0:
        for i in range(0,len(litera)):
            if litera[i] == '0':
                litera += '1'
            else:
                litera += '0'
        k -= 1
    return litera
print(transform("0",4))

lista = []
slowo = transform("0",4)
for i in range(3,len(slowo)):
    lista.append(slowo[i-3:i+1])
print(lista)
print(int("AA30",11))