import math

#
# Playing around with the Riemand zeta function 
#

primes=[2]

#
# get more primes: generates a list of primes from the initial 
# list containing only the number 2
#

for c in range(3, 100000):
	limit=int(math.sqrt(c))
	for p in primes:
		if ( (c%p)==0):
			break
		if (p>limit):
			primes.append(c)
			break

print("Number of primes:", len(primes))

# the zeta function for s real and s>1 summing up the integers

def zeta_n(s):
	z=0.0
	for i in range(1,10000):
		z=z+(1/i)**s
	return z
	
# the zeta function for s real and s>1 summing up primes 
	
def zeta_p(s):
	z=1.0
	for p in primes:
		z=z/(1-p**(-s))
	return z

# a few well known values of zeta

zeta2=3.14159265359**2/6
dn=zeta_n(2)-zeta2
dz=zeta_p(2)-zeta2
print(dn, dz, dz/dn)
print(zeta2, zeta_p(2))

zeta32=2.6123753486
print(zeta_p(3/2)-zeta32)
print(zeta_n(3/2)-zeta32)
