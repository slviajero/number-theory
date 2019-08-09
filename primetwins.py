import math
import primestuff

#
# Playing around with twins 
#
# the program calculates a few prime numbers and then searches for the twins that are a certain distance appart 
# (not only twins with a distance of 2)
#
# primes are constructed by first creating a list consisting of the first prime which is 2 and then testing numbers 

# we know that the first prime is 2 

primes=primestuff.getprimes(10000)
twins=[]
print("Number of primes:", len(primes))

#
# get the twins with a distance 2-50
#
for o in range(2,50,2):
	no=0
	for p in primes:
		if (p+o) in primes:
			no=no+1
	twins.append((o,no))
		
print(twins)




				
