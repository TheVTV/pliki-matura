

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



r2 =(trans("0", 4))

n = len(r2)


print(r2)

diff = set()

for i in range(n -3):
    seq = r2[i: i +4]
    print(seq)
    diff.add(seq)
    # print(seq)


# print(len(diff))

print(diff)

# print(r2)

# flag = True
#
# k = 0
#
# while flag:
#     res = trans("0", k)
#     ones_counter = res.count("1")
#
#     if ones_counter >= 100:
#         print(k)
#         flag = False
#
#     k+=1



# print(trans("0", 3))
# restult = (trans("0", 2))
#
#
# print(restult)
#
# suma_znakow = restult.count("1")
#
# print(suma_znakow)

# print(len(restult))

# counter = 1
# max_counter =0
#
#
# for i in range(1, len(restult) - 1):
#     curr = restult[i]
#     next = restult[i +1]
#
#     if curr == next:
#         counter += 1
#         max_counter = max(max_counter, counter)
#     else:
#         max_counter = max(max_counter, counter)
#         counter = 1
#
# max_counter = max(max_counter, counter)
#
# print(max_counter)


