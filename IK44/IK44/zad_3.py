import math

def find_factors(n):
    factors = []
    i = 2
    while n != 1:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
             i += 1
    return factors

def wrap(n):
    wraps = [0, n]
    while wraps[-1] != wraps[-2]:
        curr_sum = sum(find_factors(wraps[-1]))
        wraps.append(curr_sum)
    return wraps[1:]

#print(wrap(60))

with open('kebab.txt') as file:
    numbers = [int(n.strip()) for n in file]


def get_k(n):
    return sum(wrap(n))

print('z1')
def z_1(numbers):
    max_len = 0
    max_len_n = []
    for n in numbers:
        curr_wrap = wrap(n)
        curr_len = len(curr_wrap)
        if curr_len > max_len:
            max_len_n = []
            max_len = curr_len
            max_len_n.append(n)
        elif curr_len == max_len:
            max_len_n.append(n)
    print(max_len)
    for n in max_len_n:
        print(n)

z_1(numbers)

def is_palindrome(s):
    return s == s[::-1]

def create_sieve(n):
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0
    i = 2
    while i * i <= n:
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
        i += 1
    return sieve

def z_2(k_numbers):
    count_pal = 0
    count_prime = 0
    sieve = create_sieve(max(k_numbers))
    for n in k_numbers:
        if sieve[n]:
            count_prime += 1
        if is_palindrome(str(n)):
            count_pal += 1
    print(count_pal, count_prime)

k_numbers = [get_k(n) for n in numbers]

print('z2')


z_2(k_numbers)

print('z3')

def z_3(numbers):
    count = 0
    for n in numbers:
        curr_wrap = wrap(n)
        count_even = 0
        count_odd = 0
        for num in curr_wrap:
            if num % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        if count_even == count_odd:
            count += 1
    print(count)

z_3(numbers)


print('z4')

def dzielniki_wlasciwe(n):
    i = 1
    sum_ = 0
    while i < n:
        if n % i == 0:
            sum_ += i
        i += 1
    return sum_

def z_4(k_numbers):
    count = 0
    for n in k_numbers:
        if dzielniki_wlasciwe(n) == n:
            count += 1
    print(count)

z_4(k_numbers)

