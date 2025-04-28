def negacja(c):
    w = ""
    for i in c:
        if i == "0":
            w += "1"
        else:
            w += "0"
    return w

def transformacja(S, k):
    if k == 0:
        return S
    T = transformacja(S, k - 1)
    N = negacja(T)
    return T+N

def transformacja2(S, k):
    if S == "0":
        return transformacja(S, k - 1)

print(transformacja2("0", 7))

wynik = transformacja2("0", 7)

max_0, max_1 = 0, 0
count_0, count_1 = 0, 0

for i in wynik:
    if i == "0":
        count_0 += 1
        count_1 = 0
        if count_0 > max_0:
            max_0 = count_0
    elif i == "1":
        count_1 += 1
        count_0 = 0
        if count_1 > max_1:
            max_1 = count_1
print(max_0, max_1)
print(max(max_0, max_1))


print(transformacja2("0", 3))

wynik3 = transformacja2("0", 8)
count1 = 0
for i in wynik3:
    if i == "1":
        count1 += 1
print(count1)

print(transformacja2("0", 5))