f = open("kebab.txt", "r")
arr = []

for line in f:
    arr.append(int(line.strip()))
n = 10

def do_kebab(n):
    k = 2
    sum = 0
    while n > 1:
        while n % k == 0:
            sum += k
            n //= k
        k += 1
    return sum
help_arr = []
max_count = 0
pal_count = 0
pier_count = 0
for num in arr:
    count = 1
    liczba_kebabowa = num
    previous_kebab = do_kebab(num)
    liczba_kebabowa += previous_kebab
    while previous_kebab != do_kebab(previous_kebab):
        count +=1
        previous_kebab = do_kebab(previous_kebab)
        liczba_kebabowa += previous_kebab
        if previous_kebab == do_kebab(previous_kebab):
            liczba_kebabowa += previous_kebab
            count += 2
    if str(liczba_kebabowa) == str(liczba_kebabowa)[::-1]:
        pal_count +=1
    flag = True
    while liczba_kebabowa > 1:
        k = 2
        while liczba_kebabowa > 1 and liczba_kebabowa > k :
            if liczba_kebabowa % k == 0:
                flag = False
            k += 1
    if flag:
        pier_count += 1
print(pal_count, pier_count)