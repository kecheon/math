# coding: utf8


def isPrime(n):
    if type(n) is not int:
        print "\n Only natural number can be a prime number"
        return False
    if n <= 1:
        print "\n %d is not a prime number by definition" % (n)
        print "\n It should be greater than 1."
        return False
    if n >= 100:
        print "\n This function can test natural number less than 100"
        print "\n Please enter another number"
        return False
    else:
        return sieve(n)


def sieve(n):
    """
    A prime number is a natural number that has
    exactly two distinct natural number divisors: 1 and itself.
    To find all the prime numbers less than or equal to a given integer n
    by Eratosthenes' method:
        1. Create a list of consecutive integers
            from 2 through n: (2, 3, 4, ..., n).
        2. Initially, let p equal 2, the smallest prime number.
        3. Enumerate the multiples of p by counting to n from 2p
            in increments of p, and mark them in the list
            (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
        4, Find the first number greater than p in the list that is not marked.
            If there was no such number, stop. Otherwise,
            let p now equal this new number (which is the next prime),
            and repeat from step 3.
        5. When the algorithm terminates,
            the numbers remaining not marked in the list are
            all the primes below n.
    """

    numbers = range(2, 100)  # numbers = [2, 3, 4, ..., 99]
    marked = []
    composites = []

    for p in numbers:
        if p not in marked:
            for i in numbers:
                if p * i not in marked and p * i in numbers:
                    marked.append(p * i)
                    composites.append(p * i)

    primes = set(numbers) - set(composites)
    if n in primes:
        print "\n %d is a prime number" % (n)
        return True
    else:
        print "\n %d is not a prime number" % (n)
        return False


def test_isPrime():
    """
        A prime number (or a prime) is a natural number greater than 1
    that cannot be formed by multiplying two smaller natural numbers.
        A natural number greater than 1 that is not prime is called
    a composite number.
    """

    assert isPrime(1.5) is False
    assert isPrime(0) is False
    assert isPrime(-12) is False
    assert isPrime(1) is False
    assert isPrime(2) is True
    assert isPrime(9) is False
    assert isPrime(78) is False
    assert isPrime(83) is True
    assert isPrime(97) is True