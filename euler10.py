from primes import Primer

#
# Euler problem 10, the sum of all primes until 2000000
#
n=2000000
p=Primer(n)
print("Sum of all primes until {} is {} ".format(n, sum(p.primes)))