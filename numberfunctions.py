from math import sqrt
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
			limit=int(sqrt(c))
			for p in primes:
				if divisible(c,p):
					break
				if (p>limit):
					primes.append(c)
					break
	return primes

#
# this function determines if a number is prime relative to the 
# list of primes that is given to it, if no number from primes 
# divides n the function returns true. If n is smaller than 
# max(primes)**2 it is prime in the strict sense
#

def isprime(n, primes):
	if p in primes:
		return True
	else:
		return False

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

def congruent(i,j,m):
	return ((i%m)==(j%m))

def divisible(i,j):
	return ((i%j)==0)

def odd(n):
	return not divisible(n,2)

def even(n):
	return divisible(n,2)

#
# A class that generates a prime number calculator, stores a list of 
# primes and does things with them
#

class Primer():

	# a clumsy init function
	def __init__(self, maxprime=1000):	
		if maxprime<2:
			print("Less then 1 prime set, setting maximum to 2")
			self.getprimes(2)
		else:
			self.getprimes(maxprime)
	
	# generate an initial list of primes
	# not optimal for dynamic use	
	def getprimes(self, n):
		self.primes=[2]
		if (n>2):
			for c in range(3, n+1, 2):
				limit=int(sqrt(c))
				for p in self.primes:
					if divisible(c,p):
						break
					if (p>limit):
						self.primes.append(c)
						break

	# get the list of primes currently used either in total
	# or until a certain limit
	def list(self, n=0):
		if (n==0 or n>self.len()):
			return self.primes[:]
		else:
			return self.primes[:n]

	# how many primes do we have in total
	# or up to a certain limit
	# len(p) is an integer variant of pi(x)
	def len(self, pmax=0):
		if (pmax==0):
			return len(self.primes)
		else: 
			i=0
			for p in self.primes:
				if p>pmax:
					return i
				else:
					i=i+1

	# the maximum prime number we know for now
	def max(self):
		return self.primes[-1]

	# figure out if a number is prime 
	# for now purely on the existing number of primes	
	def isprime(self, n):
		if n in self.primes:
			return True
		else:
			return False

	# calculate the prime factors of a number n based on
	# the existing list of primes
	def factor(self, n):
		f=[]	
		for p in self.primes:
			if (n<=1):
				return f
			while divisible(n,p):
				n = n//p
				f.append(p)
		if (n>1):
			f.append(n)
		return f 
	
	# a naive way to calculate zeta from the euler formula
	# we use primes up to a maximum pmax
	def zeta(self, s, pmax=0):
		if (pmax==0):
			pmax=self.max()
		z=1.0
		for p in self.primes:
			if p>pmax:
				break
			z=z/(1-p**(-s))
		return z








