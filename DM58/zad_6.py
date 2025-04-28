lines = open("./pliki/kursanci.txt",'r').read().splitlines()

imiona = []
przedmioty = []
daty = []
godziny_rozp = []
godziny_zakon = []
stawki = []
print(lines)
for i in range(1,len(lines)):
    split_line = lines[i].split("\t")
    imie = split_line[0]
    przedmiot = split_line[1]
    data = split_line[2]
    rozpoczecie = split_line[3]
    zakonczenie = split_line[4]
    stawka = int(split_line[5])
    imiona.append(imie)
    przedmioty.append(przedmiot)
    daty.append(data)
    godziny_rozp.append(rozpoczecie)
    godziny_zakon.append(zakonczenie)
    stawki.append(stawka)

imiona_dict = {}
for imie in imiona:
    imiona_dict[imie] = []
for i in range(0,len(imiona)):
    imiona_dict[imiona[i]].append(stawki[i])
imiona_sum = {}
for imie in imiona_dict.keys():
    imiona_sum[imie] = sum(imiona_dict[imie])
print(imiona_sum)

maks_zaplata = max(imiona_sum.values())
for imie in imiona_sum.keys():
    if imiona_sum[imie] == maks_zaplata:
        print(imie, maks_zaplata)
        break


# with open("./pliki/wyniki6_2.txt",'w') as file:
#     for imie in imiona_sum.keys():
#         str_to_write = imie + ":" + str(imiona_sum[imie]) + "\n"
#         file.write(str_to_write)
pojedyncze_lekcje_counter = 0
for imie in imiona_dict:
    if len(imiona_dict[imie]) == 1:
        pojedyncze_lekcje_counter += 1
print(pojedyncze_lekcje_counter)

specjalne_nicki = []

korepetycje_dict = {}

for imie in imiona:
    korepetycje_dict[imie] = []

for i in range(0,len(imiona)):
    imie = imiona[i]
    przedmiot = przedmioty[i]
    korepetycje_dict[imie].append(przedmiot) # sa duplikaty zrobic set
for imie in imiona:
    wszystkie_przedmioty = list(set(korepetycje_dict[imie]))
    for przedmiot in wszystkie_przedmioty:
        czesc_imienia = imie[0:3].upper()
        czesc_przedmiotu = przedmiot[0:3].upper()
        ilosc_korepetycji = len(korepetycje_dict[imie])
        specjalny_nick = czesc_imienia+czesc_przedmiotu+str(ilosc_korepetycji)
        specjalne_nicki.append(specjalny_nick)
specjalne_nicki.sort()
specjalne_nicki = list(set(specjalne_nicki))
# with open("./pliki/wyniki6_4.txt",'w') as file:
#     for nick in specjalne_nicki:
#         str_to_write = nick + "\n"
#         file.write(str_to_write)

#ZASADY DO PORTFELA

#START : 21,37
#sobota rano koszt biletu 10 zl
#niedziela wieczorem koszt biletu 10 zl
#wtorki - 250 zl

#MIASTECZKO STUDENCKIE:
#Jezeli w portfelu <= 500 -> ubywa 1/5 kwoty zaokraglona w dol do groszy, min 50 zl
#Jezeli w portfelu > 500 ale <= 600 -> ubywa 1/2 portfela, w dol do groszy, min 100 zl
# portfel > 600 -> ubywa 400 zl

# 15 dzien miesiaca - 600 zl
#20 grudzien - 3 stycznia przerwa dla portfela ze wszystkiego

# 1 pazdziernika - sroda

date_translator = {}
dni_tygodnia = ['Poniedzialek','Wtorek','Sroda','Czwartek','Piatek','Sobota','Niedziela']
startowy_index = 1

for data in daty:
    date_translator[data] = dni_tygodnia[startowy_index]
    startowy_index += 1
    if startowy_index == 7:
        startowy_index = 0
print(date_translator)

portfel = 21.37
for data in daty:
    obecny_dzien = date_translator[data]