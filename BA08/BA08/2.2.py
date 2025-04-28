def JakiSystem(n):
    najw = '0'
    for char in n:
        if char > najw:
            najw = char

    if najw == 'A':
        l = 10
    elif najw == 'B':
        l = 11
    elif najw == 'C':
        l = 12
    elif najw == 'D':
        l = 13
    elif najw == 'E':
        l = 14
    elif najw == 'F':
        l = 15
    else:
        l = int(najw)


    return l + 1

f=open("liczby.txt")
liczby = [0]*15

for line in f:
    liczby[JakiSystem(line)-2] += 1
print(liczby)