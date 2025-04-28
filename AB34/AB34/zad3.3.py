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


    odd = 0
    even = 0

    for item in seq:
        if item % 2 == 0:
            even += 1
        else:
            odd +=1

    if odd == even:
        counter += 1


print(counter)


