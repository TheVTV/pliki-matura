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


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# print(is_prime(9))

# max_len = 0
# max_numbers = []

prime_counter = 0
pali_counter = 0



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

    kebabowa_liczba_str = str(kebabowa_liczba)

    kek_rev = kebabowa_liczba_str[::-1]

    if kebabowa_liczba_str == kek_rev:
        pali_counter += 1


    if is_prime(kebabowa_liczba):
        prime_counter += 1

print(pali_counter)
print(prime_counter)


