# file_name = "pliki/kebab_przyklad.txt"
file_name = "pliki/kebab.txt"


with open(file_name, "r", encoding="utf-8") as file:
    lines = [int(line.strip())for line in file]


def rlncp(n):
    czynniki = []

    i = 2

    while n > 1:
        if n % i == 0:
            czynniki.append(i)
            n = n // i
        else:
            i += 1


    czynniki_suma = sum(czynniki)

    return czynniki_suma

# print(rlncp(7))


max_len = 0
max_numbers = []


counter = 0


for number in lines:

    curr_number = number

    seq = [number]


    while True:
        res = rlncp(curr_number)

        if res in seq:
            seq.append(res)
            break
        else:
            seq.append(res)
            curr_number = res



    kebabowa_liczba = sum(seq)


    dzielniki = []

    # print(kebabowa_liczba)

    for i in range(1,kebabowa_liczba):
        # print(i)
        if kebabowa_liczba % i == 0:
            dzielniki.append(i)

    sum_dzielniki = sum(dzielniki)

    if sum_dzielniki == kebabowa_liczba:
        counter += 1


print(counter)


