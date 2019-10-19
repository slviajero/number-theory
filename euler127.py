from primes2 import Primer

prime=Primer(250000)

print(prime.len())

na=21001
nb=21051

def res(n):
	if n>=len(prime.primes):
		raise ValueError
	p=prime.primes[n-1]
	return ((p+1)**n+(p-1)**n)%p**2

for i in range(na,nb,2):
	print(i, res(i))




