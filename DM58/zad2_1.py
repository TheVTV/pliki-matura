litery = ['A','B','C','D','E','F']
liczby = ['2','3','4','5','6','7','8','9']


def znajdz_litere(n,litera):
    for char in n:
        if char == litera:
            return True
    return False

def funkcja(n):
    curr_max = 2
    i = 0
    while i < len(litery):
        if znajdz_litere(n,litery[i]) == True:
            if 10+i+1 > curr_max:
                curr_max = 10+i+1
        i += 1
    j = 0
    while j < len(liczby):
        if znajdz_litere(n,liczby[j]) == True:
            if 3+j > curr_max:
                curr_max = 3+j
        j += 1
    return curr_max
print(funkcja("AA30"))