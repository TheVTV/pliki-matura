

def negacja(ciag):
    res = ""
    for sign in ciag:
        if sign == "0":
            res += "1"
        else:
            res += "0"
    return res


def trans(s, k):
    if k == 0:
        return s
    else:
        t = trans(s, k-1)
        n = negacja(t)
        return t +n


# print(trans("0", 3))
print(trans("101", 3))