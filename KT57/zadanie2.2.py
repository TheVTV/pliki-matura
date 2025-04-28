def znajdz_podstawe(a, b):
    for podstawa in range(2, 17):
        try:
            a_dec = int(a, podstawa)
            b_dec = int(b, podstawa)
            b_dec_odwrocone = int(str(b_dec)[::-1])
            if a_dec == b_dec_odwrocone:
                return podstawa
        except:
            pass
    return None

systemy = [0] * 17

with open("liczby.txt", "r") as plik:
    for linia in plik:
        a, b = linia.strip().split('\t')
        system = znajdz_podstawe(a, b)
        if system:
            systemy[system] += 1

for i in range(2, 17):
    if systemy[i] > 0:
        print(f"{i}: {systemy[i]}")
