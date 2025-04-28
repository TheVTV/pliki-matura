def znajdz_podstawe(a, b):
    for podstawa in range(2, 17):
        try:
            a_dec = int(a, podstawa)
            b_dec = int(b, podstawa)
            if a_dec == int(str(b_dec)[::-1]):
                return podstawa
        except:
            pass
    return None

najwieksza = ("", -1, -1)
najmniejsza = ("", -1, float("inf"))

with open("liczby.txt", "r") as plik:
    for linia in plik:
        a, b = linia.strip().split('\t')
        system = znajdz_podstawe(a, b)
        if system:
            wartosc = int(a, system)
            if wartosc > najwieksza[2]:
                najwieksza = (a, system, wartosc)
            if wartosc < najmniejsza[2]:
                najmniejsza = (a, system, wartosc)

print(f"{najmniejsza[0]} {najwieksza[0]}")