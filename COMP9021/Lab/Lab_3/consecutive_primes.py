# Finds all sequences of consecutive prime 5-digit numbers,
# say (a, b, c, d, e, f), such that
# b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.


# Insert your code here

def is_prime_number(number):
    is_prime = True
    for i in range(2, number // 2):
        if number % i == 0:
            is_prime = False
            break
    return is_prime

def find_all_primes():
    all_primes = []
    for i in range(10000, 100000):
        if is_prime_number(i):
            all_primes.append(i)
        
    return all_primes

def find_consecutive_primes(all_primes):
    consecutive_primes = []
    for i in range(len(all_primes) - 5):
        if all_primes[i] == all_primes[i + 1] - 2 and \
           all_primes[i + 1] == all_primes[i + 2] - 4 and \
           all_primes[i + 2] == all_primes[i + 3] - 6 and \
           all_primes[i + 3] == all_primes[i + 4] - 8 and \
           all_primes[i + 4] == all_primes[i + 5] - 10:
            consecutive_primes.append([all_primes[i], all_primes[i + 1], \
                                       all_primes[i + 2], all_primes[i + 3], \
                                       all_primes[i + 4], all_primes[i + 5]])
    return consecutive_primes

all_primes = find_all_primes()
consecutive_primes = find_consecutive_primes(all_primes)

# Print the solutions
print("The solutions are:\n")
for i in range(len(consecutive_primes)):
    output = ''
    for j in range(5):
        output += str(consecutive_primes[i][j]) + ' '
    output += str(consecutive_primes[i][5])
    print(output)
