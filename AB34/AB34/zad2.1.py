

n = "1BCD9"




n_len = len(n)


min_system = 0

for i in range(n_len):
    digit = n[i]

    if digit == "2":
        min_system = 3
    elif digit == "3":
        min_system = 4
    elif digit == "4":
        min_system = 5
    elif digit == "5":
        min_system = 6
    elif digit == "6":
        min_system = 7
    elif digit == "7":
        min_system = 8
    elif digit == "8":
        min_system = 9
    elif digit == "9":
        min_system = 10
    elif digit == "A":
        min_system = 11
    elif digit == "B":
        min_system = 12
    elif digit == "C":
        min_system = 13
    elif digit == "D":
        min_system = 14
    elif digit == "E":
        min_system = 15
    elif digit == "F":
        min_system = 16


print(min_system)

k = 17 - min_system



print(k)