from primes2 import Primer

p=Primer()
n=len(p)

for i in range(n,10001):
	q=p.next()

print(q)
print(p.primes[0])
print(p.primes[10000])

list=p.until(200)
print(list)