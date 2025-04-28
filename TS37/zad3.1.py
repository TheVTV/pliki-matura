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
for num in arr:
    count = 1
    previous_kebab = do_kebab(num)
    while previous_kebab != do_kebab(previous_kebab):
        count +=1
        previous_kebab = do_kebab(previous_kebab)
        if previous_kebab == do_kebab(previous_kebab):
            count += 2
    if count == max_count:
        help_arr.append(num)
    if max_count < count:
        max_count = count
        help_arr.clear()
        help_arr.append(num)

print(max_count, help_arr)