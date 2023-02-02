def test_prime(val):
    for d in range(2,int(val**.5)+1):
        if val % d == 0 and d != val:
            return False
    return True

def list_primes(max_num):
    primes = []
    for i in range(2, max_num + 1):
        if test_prime(i):
            primes.append(i)
    yield primes          


print([i for i in list_primes(99000)])            