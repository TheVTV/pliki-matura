f = open("liczby_przyklad.txt", "r")
arr = []

for line in f:
    arr.append(line.strip().split())

a = "0123456789ABCDEF"
dict_systemy = {}
print(arr)
for pair in arr:
    stac = []
    for char1 in pair[0]:
        stac.append(char1)
    for char2 in pair[1]:
        stac.append(char2)
    max_val = max(stac)
    for i in range(len(a)):
        if a[i] == max_val:
            test = a[i]
            dict_systemy[i + 1] = dict_systemy.get(i+1, 0) + 1
            break


print(dict_systemy)