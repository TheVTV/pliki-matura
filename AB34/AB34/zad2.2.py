from collections import defaultdict

# file_name = "pliki/liczby_przyklad.txt"
file_name = "pliki/liczby.txt"


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

    sys_dict[min_line_system] += 1

# print(sys_dict)


dict_sorted = sorted(sys_dict.items())

# print(dict_sorted)

for i in range(len(dict_sorted)):
    print(dict_sorted[i][0],":", dict_sorted[i][1])


# print(dict_sorted)

# for key, value in dict_sorted.items()

    # print(min_line_system)

    # n1_dec = int(n1, min_line_system)
    # n2_dec = int(n2, min_line_system)
    #
    #
    # n2_dec_rev = str(n2_dec)[::-1]
    #
    # print(n1_dec, n2_dec_rev)


    # print(n1_dec)

    # print(min_line_system)

    # sys_dict[line_system] += 1



# print(sys_dict)





# # # print(lines)
# #
# res_dict = defaultdict(int)
#
#
# for line in lines:
#
#     number1 = line[0]
#     number2 = line[1]
#
#
#     min_sys_dict = {"0": 2, "1": 2,"2":3, "3": 4, "4": 5, "5": 6, "6": 7, "7": 8, "8": 9, "9": 10, "A": 11, "B": 12, "C": 13, "D": 14, "E": 15, "F":16 }
#
#     number_min_sys = 2
#
#     for sign in number1:
#         if sign == "0" or sign == "1":
#             continue
#         min_sys = min_sys_dict[sign]
#
#         number_min_sys = max(number_min_sys, min_sys)
#
#
#     for sign in number2:
#         if sign == "0" or sign == "1":
#             continue
#         min_sys = min_sys_dict[sign]
#
#         number_min_sys = max(number_min_sys, min_sys)
#
#     # print(number_min_sys)
#
#     res_dict[number_min_sys] += 1
#
#
#     # sys = 0
#     #
#     #
#     # for sign in number1:
#     #     if sign.isdigit():
#     #         sys = max(sys, int(sign) + 1)
#     #     else:
#     #         if sign == "A":
#     #             sys = max(sys, 11)
#     #         elif sign == "B":
#     #             sys = max(sys, 12)
#     #         elif sign == "C":
#     #             sys = max(sys, 13)
#     #         elif sign == "D":
#     #             sys = max(sys, 14)
#     #         elif sign == "E":
#     #             sys = max(sys, 15)
#     #         elif sign == "F":
#     #             sys = max(sys, 16)
#     #
#     # res_dict[sys] += 1
#
# print(res_dict)