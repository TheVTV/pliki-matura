lines = open("./pliki/kebab.txt",'r').read().splitlines()

def rozloz_na_czynniki(liczba):
    start = 2
    czynniki = []
    while liczba > 1:
        if liczba % start == 0:
            czynniki.append(start)
            liczba = liczba / start
            start = 2
        else:
            start += 1
    return czynniki

def sprawdz_dzielniki(liczba):
    dzielniki = []
    for i in range(1,liczba):
        if liczba % i == 0:
            dzielniki.append(i)
    return dzielniki

def zkebab(liczba):
    czynniki = rozloz_na_czynniki(liczba)
    return sum(czynniki)

def check_if_pierwsza(liczba):
    if liczba == 0 or liczba == 1:
        return False
    if liczba == 2:
        return True
    if liczba % 2 == 0:
        return False
    for i in range(3,liczba,2):
        if liczba % i == 0:
            return False
    return True

counter_kebsy_palindromy = 0
counter_kebsy_pierwsze = 0
test = []
kebab_dict = {}
counter_suma_kebsow_p_np = 0
counter_falafel = 0
for line in lines:
    oryg_liczba = int(line)
    liczba = int(line)
    prev_liczba = liczba
    zkebsione = [oryg_liczba]
    counter = 1
    while True:
        liczba = zkebab(liczba)
        counter += 1
        if liczba == prev_liczba:
            zkebsione.append(liczba)
            break
        prev_liczba = liczba
        zkebsione.append(liczba)

    suma_zkebsionych = sum(zkebsione)

    czynniki_zkebsionej = sprawdz_dzielniki(suma_zkebsionych)
    suma_czynnikow_zkebsionej = sum(czynniki_zkebsionej)
    if suma_czynnikow_zkebsionej == suma_zkebsionych:
        print(czynniki_zkebsionej,suma_zkebsionych)
        counter_falafel += 1

    if check_if_pierwsza(suma_zkebsionych):
        counter_kebsy_pierwsze += 1

    string_sumy = str(suma_zkebsionych)

    if string_sumy == string_sumy[::-1]:
        counter_kebsy_palindromy += 1

    np = 0
    p = 0
    for liczba in zkebsione:
        if liczba % 2 == 0:
            p += 1
        else:
            np += 1

    if p == np:
        counter_suma_kebsow_p_np += 1

    test.append(counter)
    if counter not in kebab_dict.keys():
        kebab_dict[counter] = [oryg_liczba]
    else:
        kebab_dict[counter].append(oryg_liczba)
maks = max(test)
print(maks)
for liczba in kebab_dict[maks]:
    print(liczba) # odpowiedz do 3.1
# print(counter_kebsy_palindromy)
# print(counter_kebsy_pierwsze)
# print(counter_suma_kebsow_p_np)
print(counter_falafel)
