# n = "1BCE9"
# systems = -1
# m = -1
# czy_jest_literka = False
# last_system = -1
# for i in range(len(n)):
#     indeks = -1
#     for j in range(len(literki)):
#         if n[i] == literki[j]:
#             czy_jest_literka = True
#             if j > indeks:
#                 indeks = j
#     if czy_jest_literka:
#         temp = 16- (10+indeks)
#         if temp < last_system:
#             systems = temp
#         last_system = temp
#
#
# if not czy_jest_literka:
#     for j in range(len(n)):
#         if m < int(n[j]):
#             m = int(n[j])
#     systems = 16-m
#     print(systems)
# else:
#     print(systems)
n = "A"
L = len(n)

def ilosc_dozwolonych(n, L):
    max_ord_val = -1
    for i in range(L):
        val = ord(n[i])
        if val > max_ord_val:
            max_ord_val = val

    if max_ord_val >= 65:
        return ord("F") - max_ord_val + 1
    else:
        return 16-(max_ord_val - ord("0"))


print(ilosc_dozwolonych(n, L))


