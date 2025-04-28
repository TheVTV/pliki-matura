data = []
with open("liczby_przyklad.txt", "r") as file:
    for row in file.read().split("\n"):
        if row != "":
            data.append(row.split("\t"))
print(data)
file.close()

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

s = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

def to_dec(num:str, base: int):
    result = 0
    n = len(num) - 1
    iterator = 0
    while n >= 0:
        if num[n] not in s.keys():
            result += int(num[n]) * base ** iterator
        else:
            pass
        n-=1
        iterator += 1
    return result



print(to_dec("777", 2))

systems = {i : 0 for i in range(2, 17)}

for row in data:
    first = row[0]
    second = row[1]

print(systems)
