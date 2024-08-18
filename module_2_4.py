numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
a = 0
is_prime = True
for i in range(1, len(numbers)):
    end = (numbers[i] // 2) + 1
    for j in range(2, end):
        is_prime = (numbers[i] % j == 0)
        if is_prime:
            not_primes.append(numbers[i])
            break
    else:
        primes.append(numbers[i])
print("Primes: ", primes)
print("Not Primes: ", not_primes)

