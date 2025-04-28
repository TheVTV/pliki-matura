lines = open("./pliki/liczby.txt",'r').read().splitlines()

dict_systemow = {}

for i in range(2,17):
    dict_systemow[i] = 0

def converter_na_dziesietne(napis,system):
    return int(napis,system)

litery = ['A','B','C','D','E','F']
liczby = ['2','3','4','5','6','7','8','9']

def znajdz_litere(n,litera):
    for char in n:
        if char == litera:
            return True
    return False

def funkcja(n):
    curr_max = 2
    i = 0
    while i < len(litery):
        if znajdz_litere(n, litery[i]) == True:
            if 10 + i + 1 > curr_max:
                curr_max = 10 + i + 1
        i += 1
    j = 0
    while j < len(liczby):
        if znajdz_litere(n, liczby[j]) == True:
            if 3 + j > curr_max:
                curr_max = 3 + j
        j += 1
    return curr_max

curr_min = 9999999999999999999
curr_max = 0
true_min = ""
true_max = ""
pierwsze_liczby = []
drugie_liczby = []

for line in lines:
    split_line = line.split("\t")
    pierwsza_liczba = split_line[0]
    druga_liczba = split_line[1]
    print(pierwsza_liczba)
    print(druga_liczba)
    system = funkcja(pierwsza_liczba)
    system_dwa = funkcja(druga_liczba)
    print(system_dwa)
    ostateczny_system = max(system_dwa, system)
    while True:
        converted_pierwsza = str(converter_na_dziesietne(pierwsza_liczba,ostateczny_system))
        converted_druga = str(converter_na_dziesietne(druga_liczba, ostateczny_system))
        print(converted_druga)
        print(converted_pierwsza)
        print("-----------")
        if converted_druga[::-1] == converted_pierwsza:
            break
        else:
            ostateczny_system += 1
    true_pierwsza = converter_na_dziesietne(pierwsza_liczba,ostateczny_system)
    true_druga = converter_na_dziesietne(druga_liczba,ostateczny_system)
    if true_pierwsza > curr_max:
        true_max = pierwsza_liczba
        curr_max = true_pierwsza
    if true_druga > curr_max:
        true_max = druga_liczba
        curr_max = true_druga
    if true_pierwsza < curr_min:
        true_min = pierwsza_liczba
        curr_min = true_pierwsza
    if true_druga < curr_min:
        true_min = druga_liczba
        curr_min = true_druga
    dict_systemow[ostateczny_system] += 1
    pierwsze_liczby.append(pierwsza_liczba)
    drugie_liczby.append(druga_liczba)
# with open("./wyniki2.txt",'w') as file:
#     for key in dict_systemow:
#         str_to_write = str(key) + ":"+str(dict_systemow[key]) +"\n"
#         file.write(str_to_write)
print(true_min,true_max)

znaki_dict = {}

total = 0
for i in range(0,len(pierwsze_liczby)):
    pierwsza_liczba = pierwsze_liczby[i]
    druga_liczba = drugie_liczby[i]
    for char in pierwsza_liczba:
        if char not in znaki_dict.keys():
            znaki_dict[char] = 1
        else:
            znaki_dict[char] += 1
        total += 1
    for char in druga_liczba:
        if char not in znaki_dict.keys():
            znaki_dict[char] = 1
        else:
            znaki_dict[char] += 1
        total += 1
avg_dict = {}
for key in znaki_dict:
    avg_dict[key] = str(round((znaki_dict[key]/total)*100,2)) + "%"
print(avg_dict)

with open("./wyniki24.txt",'w') as file:
    for key in avg_dict:
        str_to_write = key + ":" + avg_dict[key] + "\n"
        file.write(str_to_write)