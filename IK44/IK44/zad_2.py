with open('liczby.txt') as file:
    pairs = [l.strip().split('\t') for l in file]

print('z2')



print('z4')

def z_4(pairs):
    digits = [str(i) for i in range(10)]
    l = [chr(n) for n in range(65, 71)]
    digits.extend(l)
    frequency = {n : 0 for n in digits}
    character_count = 0
    for s, s1 in pairs:
        for c in s + s1:
            character_count += 1
            frequency[c] += 1
    for key, freq in frequency.items():
        print(key,':', round((freq / character_count) * 100, 2), '%')


z_4(pairs)