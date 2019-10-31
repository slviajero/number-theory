from primes import Primer

#
# Solution of Euler 7, compute the 10000 th prime number
#

p=Primer()
n=len(p)

for i in range(n,10001):
	q=p.next()

print("Prime number 10000 is {} ".format(q))



