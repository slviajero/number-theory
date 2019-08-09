import math
#
# this function generates the prime numbers up to the limit of n
# we start from a list just containing 2, test numbers from 3 upwards, step 2
# we only need to test factors from the list of primes up to the 
# square root of the number in question
#

def getprimes(n):
	primes=[2]
	if (n>2):
		for c in range(3, n+1, 2):
			limit=int(math.sqrt(c))
			for p in primes:
				if ( (c%p)==0):
					break
				if (p>limit):
					primes.append(c)
					break
	return primes

#
# factorize an integer n based on the list of primes supplied in the argument
# the function does not find all factors but just the ones in the list
#
def factor(n, primes):
	f=[]	
	for p in primes:
		if (n<=1):
			return f
		while (n%p == 0):
			n = int(n/p)
			f.append(p)
	if (n>1):
		f.append(n)
	return f

#
# euklids algorithm to find the greatest common divisor of two integers
# non recursive for a change
# no optimization like for example handling situation where one factor is 
# much bigger than the other
#
def euklid1(i,j):
	if (i<1 or j<1):
		return 0
	while (i!=j):
		if (i>j):
			i=i-j
		else:
			j=j-i
	return j

def euklid(i,j):
	return euklid1(i,j)

def coprime(i,j):
	return euklid(i,j)==1




