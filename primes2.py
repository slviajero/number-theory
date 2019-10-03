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
		self.primes=[2, 3]
		self.debug=debug
		if maxprime>2:
			self.getprimes(maxprime)
		# safety net for dynamic next

	def setdebug(self, debug):
		self.debug=debug

#
# generate an initial list of primes starting from the knowledge that 
# 2 and 3 are prime. All other primes are generated dynamically	
#
	def getprimes(self, n):
	
		pmax=self.primes[-1]

		# we have already all we need
		if (n<=pmax):
			return
		
		if self.debug:
			print("Having {} primes until maximum {}. Getting primes until {}".format(len(self.primes),pmax,n))
		
		# Using the next function to find all the next primes until n
		while self.next()<n:
			continue

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

	def __len__(self):
		return len(self.primes)

	# the maximum prime number we know for now
	def max(self):
		return self.primes[-1]

	def __iter__(self):
		self.index=0
		return self

	def __next__(self):
		if (self.index==len(self)):
			raise StopIteration
		else:
			p=self.primes[self.index]
			self.index+=1
			return p

	# get the next prime, we start from a list of known primes and 
	# take the maximum plus 2 and divide until we exceed the sqrt
	# we know that the candidate has to be prime if none of the smaller
	# primes divide it 
	def next(self):
		i=self.max()
		while True:
			i=i+2
			limit=int(sqrt(i)+0.5)
			for p in self.primes:
				if p>limit:
					self.primes.append(i)
					return i
				if self.divisible(i,p):
					break

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
# all the magic now encapsulated in the Factorizer
#
	def factor(self, n):
			
		if self.debug:
			no=n
			cl=perf_counter()

		f=[]
		fact=Factorizer(n, self)
		for i in fact:
			f.append(i)

		if self.debug:
			cl=perf_counter()-cl
			print("Factor for {} elapsed time {} seconds".format(no, cl))

		return f 

#
# Return a new factorizer with knowledge about our primes
#
	def getfactorizer(self, n):
		f=Factorizer(n, self)
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


# Factorizer that uses the next function of its primer object

class Factorizer: 

	# a Factorizer either gets a primer (that stores all the primes)
	# or it makes one

	def __init__(self, n=1, primer=None):
		if primer==None:
			self.primer=Primer()
		else:
			self.primer=primer
		self.init(n)

	def init(self, n):

		# set a new number to be factorized
		# self.factors stores the factors for reuse 
		# self.__factors__ is used as a temp var
		self.a=n
		self.n=n
		self.factors=[]
		self.__factors__=[]
		self.done=False
		return self

	def __next__(self): 

		# in case we know the factors already
		if self.done:
			if self.__factors__==[]:
				self.__factors__=self.factors[:]
			if len(self.__factors__)>0:
				return self.__factors__.pop(0)
			else:
				raise StopIteration
			

		# nothing to factorize any more
		if self.a==1:
			self.done=True
			raise StopIteration

		# is any of the known primes a factor

		for p in self.primer.primes:
			if self.primer.divisible(self.a, p):
				self.a=self.a//p
				self.factors.append(p)
				return p

		# have we tested all the primes up to the sqrt

		p=self.primer.max()
		limit=int(sqrt(self.a)+0.5)
		while p<limit:
			p=self.primer.next()
			if self.primer.divisible(self.a, p):
				self.a=self.a//p
				self.factors.append(p)
				return p

		# all the tests passed, self.a is prime

		p=self.a
		self.a=1
		self.factors.append(p)
		return p

	def __iter__(self):
		self.a=self.n
		return self

	def __len__(self):
		fi=iter(self)
		i=0
		for f in fi:
			i+=1
		return i








