def negacja(c):
    w = ""
    for z in c:
        if z == "0":
            w += "1"
        else:
            w += "0"
    return w

def transformacja(s,k):
    if k == 0:
        return s
    else:
        t = transformacja(s,k-1)
        n = negacja(t)
        return t + n
t = transformacja("0",4)
print(t)

# zlicz unikalne podciagi
p = []

for i in range(len(t)):
    # i = ostatni element ciagu
    for j in range(0,i):
        # j = pierwszy element ciagu (bez i)
        podciag = t[j:i+1]
        # print("i: ", i)
        # print("j: ", j)
        # print("podciag : ", podciag )
        if len(podciag) == 4 and podciag not in p:
            p.append(podciag)

print(p)
print(len(p))