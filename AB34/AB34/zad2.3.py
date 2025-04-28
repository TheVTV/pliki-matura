from collections import defaultdict

file_name = "pliki/liczby_przyklad.txt"
# file_name = "pliki/liczby.txt"


with open(file_name, "r", encoding="utf-8") as file:
    lines = [line.strip().split() for line in file]


sys_dict = defaultdict(int)


def system(n):

    l = len(n)

    max_sys = 2

    for i in range(l):
        item = n[i]

        item_ord = ord(item)

        sys = -1

        if item_ord <= 57:
            sys = item_ord - 47
        else:
            sys = item_ord - 54

        # print(sys)
        if sys > max_sys:
            max_sys = sys

    return max_sys

# print(system("1BCD9"))

max_number = 0
max_pierw = ""
min_number = float("inf")
min_pierw = ""

for line in lines:


    n1 = line[0]
    n2 = line[1]


    min_line_system = max(system(n1), system(n2))

    # flag = True


    while True:
        n1_dec = int(n1, min_line_system)
        n2_dec = int(n2, min_line_system)


        n2_dec_rev = str(n2_dec)[::-1]
        n1_dec_str = str(n1_dec)


        if n1_dec_str == n2_dec_rev:
            break
        else:
            min_line_system += 1


    dec1_number = int(n1, min_line_system)
    dec2_number = int(n2, min_line_system)



    if dec1_number > max_number:
        max_number = dec1_number
        max_pierw = n1

    if dec2_number > max_number:
        max_number = dec2_number
        max_pierw = n2

    if dec1_number < min_number:
        min_number = dec1_number
        min_pierw = n1

    if dec2_number <  min_number:
        min_number = dec2_number
        min_pierw = n2


print(min_pierw)
print(max_pierw)