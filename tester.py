import primestuff
import math

#list=[]

#list=primestuff.getprimes(10000)

#print(primestuff.factor(256, list))

#print(primestuff.euklid1(24,150012))

#print(primestuff.euklid(24,15))

#print(primestuff.coprime(8,5))

primes=primestuff.Primer(100)

print(primes.list())

print(primes.list(20))

print("Number of primes: ", primes.len())
print("Maximum prime: ", primes.max())

print("Number of primes until ...", primes.len(11))

#print(primes.isprime(8))

#print(primes.factor(1000))

zeta2=3.14159265359**2/6
print(primes.max())

#for i in range(100,1000,100):
#	delta=zeta2-primes.zeta(2,i)
#	print(i, delta, math.log(delta))

