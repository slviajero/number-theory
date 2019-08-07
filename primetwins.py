import math

#
# Playing around with twins
#

primes=[2]
twins=[]

#
# get more primes
#

for c in range(3, 10000):
	limit=int(math.sqrt(c))
	for p in primes:
		if ( (c%p)==0):
			break
		if (p>limit):
			primes.append(c)
			break

print("Number of primes:", len(primes))

for o in range(2,50,2):
	no=0
	for p in primes:
		if (p+o) in primes:
			no=no+1
	twins.append((o,no))
		
print(twins)




				
