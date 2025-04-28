n = "2025"

z = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
l = 15

maxSystem = 16

for i in n:
    for j in range(15):
        if i == z[j]:
            if maxSystem > 15 - j:
                maxSystem = 15 - j

print(maxSystem)
