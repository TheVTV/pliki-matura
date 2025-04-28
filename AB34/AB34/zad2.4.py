from collections import defaultdict

# file_name = "pliki/liczby_przyklad.txt"


file_name = "pliki/liczby.txt"


with open(file_name, "r", encoding="utf-8") as file:
    lines = [line.strip().split() for line in file]


signs_dict = defaultdict(int)


sings_amount = 0


for line in lines:
    number1 = line[0]
    number2 = line[1]

    for i in range(len(number1)):
        signs_dict[number1[i]] += 1
        sings_amount += 1

    for j in range(len(number2)):
        signs_dict[number2[j]] += 1
        sings_amount += 1


# print(sings_amount)

# print(signs_dict)


percent_dict = defaultdict(str)


for key, value in signs_dict.items():
    percent = round((value / sings_amount) * 100, 2)


    percent_str = str(percent)+"%"

    percent_dict[key] = percent_str


dict_sort = sorted(percent_dict.items())

for key, value in dict_sort:
    print(key,":", value)