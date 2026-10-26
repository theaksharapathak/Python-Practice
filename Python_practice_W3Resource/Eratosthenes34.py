# Compute Primes Using Sieve of Eratosthenes
def prime_erato(n):
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            print(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)


prime_erato(10)
