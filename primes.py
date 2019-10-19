from math import sqrt
from time import perf_counter

#
# A class that generates a prime number calculator, stores a list of 
# primes and does things with them
#

class Primer():

#
# an init function, default is to generate primes up to 1000
#
	def __init__(self, maxprime=1000, debug=False):	
		self.primes=[2]
		self.debug=debug
		if maxprime>2:
			self.getprimes(maxprime)

	def setdebug(self, debug):
		self.debug=debug

#
# generate an initial list of primes starting from the knowledge that 
# 2 and 3 are prime. All other primes are generated dynamically	
#
	def getprimes(self, n):
		# super clumsy init - need rework later
		pmax=self.primes[-1]
		if (n<=pmax):
			return
		# avoid the even trap
		if pmax==2:
			self.primes.append(3)
			pmax=3
		# the main loop
		if self.debug:
			print("Having {} primes until maximum {}. Getting primes until {}".format(len(self.primes),pmax,n))
		for c in range(pmax, n+1, 2):
			limit=int(sqrt(c))
			for p in self.primes:
				if self.divisible(c,p):
					break
				if (p>limit):
					self.primes.append(c)
					break
		if self.debug:
			print("Having {} primes until {}".format(len(self.primes), self.primes[-1]))

#
# get the list of primes currently used either in total
# or until a certain limit
#
	def list(self, n=0):
		if (n==0 or n>self.len()):
			return self.primes[:]
		else:
			return self.primes[:n]

#
# get the list of primes currently used either in total
# or until a certain limit
#
	def until(self, n):
		if n>self.primes[-1]:
			self.getprimes(n+1)
		result=[]
		for p in self.primes:
			if p<=n:
				result.append(p)
			else: 
				break
		return result

#
# how many primes do we have in total
# or up to a certain limit
# len(p) is an integer variant of pi(x)
#
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

#
# figure out if a number is prime 
# this program uses first the list of known primes 
# and then tries to factor the number 	
#
	def isprime(self, n):
		#is it in the list -> good
		if n in self.primes:
			return True
		else:
		# if not, try to factor it (dynamically generating more primes)
			result=self.factor(n)
			if result==[n]:
				return True
			else:
				return False

#
# calculate the prime factors of a number n based on
# the existing list of primes, this is extended if needed
#
	def factor(self, n):
		f=[]	
		if self.debug:
			no=n
			cl=perf_counter()

		# find all the factors that we have already in primes
		for p in self.primes:
			if (n<=1):
				return f
			while self.divisible(n,p):
				n = n//p
				f.append(p)

		if self.debug:
			print("Factored {} with primes until {} ".format(no, self.max()))
		
		if (n>1):
			
			if self.debug:
				print("Remains {} unfactored".format(n))

			limit=int(sqrt(n))
			if self.max()<limit:
				if self.debug:
					print("Lowest prime below needed limit. Getting more until", limit)
				
				# generating primes until the needed maximum

				pm1=self.len()
				self.getprimes(limit)
				pm2=self.len()
				newprimes=self.primes[pm1:pm2]
				for p in newprimes:
					if (n<=1):
						return f
					while self.divisible(n,p):
						n = n//p
						f.append(p)
			# if the primes until sqrt(n) yield no factorization 
			f.append(n)

		if self.debug:
			cl=perf_counter()-cl
			print("Factor for {} elapsed time {} seconds".format(no, cl))

		return f 

#	
# a naive way to calculate zeta from the euler formula
# we use primes up to a maximum pmax
#
	def zeta(self, s, pmax=0):
		if (pmax==0):
			pmax=self.max()
		z=1.0
		for p in self.primes:
			if p>pmax:
				break
			z=z/(1-p**(-s))
		return z
#
# number theory helper functions put inside the class
# this could be used stand alone as well
#
	def euklid(self,i,j):
		if (i<1 or j<1):
			return 0
		while (i!=j):
			if (i>j):
				i=i-j
			else:
				j=j-i
		return j

	def coprime(self,i,j):
		return self.euklid(i,j)==1

	def congruent(self,i,j,m):
		return ((i%m)==(j%m))

	def divisible(self,i,j):
		return ((i%j)==0)

	def odd(self,n):
		return not self.divisible(n,2)

	def even(self,n):
		return self.divisible(n,2)
#
# Save the prime numbers generated to a file 
#
	def save(self, filename):
		with open(filename,"w") as f:
			for p in self.primes:
				f.write("{}\n".format(p))
#
# load a list of prime numbers into the class - no health check!
#
	def load(self, filename):
		with open(filename,"r") as f:
			self.primes=[]
			for line in f.readlines():
				try:
					self.primes.append(int(line))
				except ValueError:
					print("Wrong value {} dropped".format(line))









