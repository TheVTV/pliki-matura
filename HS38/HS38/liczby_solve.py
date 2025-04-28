wejscie = open("liczby.txt", "r")
wyjscie = open("wyniki2.txt", "w")

dane = [line.strip().split() for line in wejscie.readlines()]

# print(dane)

def find_min_base(n):
    maxi = 0
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(n)):
        znak = n[i]
        for j in range(len(digits)):
            if digits[j] == znak:
                if j > maxi:
                    maxi = j

    base = maxi + 1
    return base
def find_base(l1, l2):
    start_b = max(find_min_base(l1), find_min_base(l2))
    for b in range(start_b, 16 + 1):
        if list(str(int(l1, b))) == list((reversed(str(int(l2, b))))):
            return b
    return None

def zadanie22(dane, wyjscie):
    print("2.2.", file = wyjscie)

    bases_count = {"2":0,
                     "3":0,
                     "4":0,
                     "5":0,
                     "6": 0,
                     "7": 0,
                     "8": 0,
                     "9": 0,
                     "10": 0,
                     "11": 0,
                     "12": 0,
                     "13": 0,
                     "14":0,
                     "15":0,
                     "16":0
                     }

    for para in dane:
        liczba1, liczba2 = para[0], para[1]
        base = find_base(liczba1, liczba2)
        bases_count[str(base)] += 1

    for key, value in bases_count.items():
        print(f"{key}: {value}", file = wyjscie)

def zadanie23(dane, wyjscie):
    print("2.3.", file = wyjscie)
    min_global_dec = float("inf")
    maxi_global_dec = float("-inf")

    min_global_base = ""
    maxi_global_base = ""

    for para in dane:
        liczba1, liczba2 = para[0], para[1]
        base = find_base(liczba1, liczba2)

        liczba1_dec, liczba2_dec = int(liczba1, base), int(liczba2, base)

        if liczba1_dec > maxi_global_dec:
            maxi_global_dec = liczba1_dec
            maxi_global_base = liczba1
        if liczba2_dec > maxi_global_dec:
            maxi_global_dec = liczba2_dec
            maxi_global_base = liczba2

        if liczba1_dec < min_global_dec:
            min_global_dec = liczba1_dec
            min_global_base = liczba1

        if liczba2_dec < min_global_dec:
            min_global_dec = liczba2_dec
            min_global_base = liczba2

    print(min_global_base, maxi_global_base, file = wyjscie)

def zadanie24(dane, wyjscie):
    print("2.4.", file=wyjscie)
    total_count = 0

    count_symb = {"0":0,
                  "1":0,
                  "2":0,
                  "3":0,
                  "4": 0,
                  "5": 0,
                  "6": 0,
                  "7": 0,
                  "8": 0,
                  "9": 0,
                  "A": 0,
                  "B": 0,
                  "C": 0,
                  "D": 0,
                  "E": 0,
                  "F": 0,
                  }

    for para in dane:
        liczba1, liczba2 = para[0], para[1]
        total_count += (len(liczba1) + len(liczba2))
        for symb in count_symb.keys():
            count_symb[symb] += ( liczba1.count(symb) + liczba2.count(symb) )

    for symb, count in count_symb.items():
        print(f"{symb} : { round((count/total_count ) * 100, 2)}%", file = wyjscie)

zadanie22(dane, wyjscie)
zadanie23(dane, wyjscie)
zadanie24(dane, wyjscie)

wejscie.close()
wyjscie.close()