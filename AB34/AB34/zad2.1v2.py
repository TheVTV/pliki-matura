


n = "2139"

l = 4

# n = "1BCD9"

# l = 5


max_sys = 2


for i in range(l):
    item = n[i]

    item_ord = ord(item)

    # print(item)

    sys = -1


    if item_ord <= 57:
        sys = item_ord - 47
    else:
        sys = item_ord - 54

    # print(sys)
    if sys > max_sys:
        max_sys = sys


k = (16 - max_sys) + 1

# print(sys)

print(k)