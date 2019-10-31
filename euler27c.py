from primes import Primer

#
# in this version the class EulerPolynomial extends the Primer class
# by a function for quadratic polynomials and their degree measured in the 
# consecutive primes it produces
#
# The methods f(), new(), and deg() have been added

class EulerPolynomial(Primer):

	def __init__(self, a=1, b=41, debug=False):
		self.debug_e=debug
		self.a=a
		self.b=b
		self.pprimes=[]
		super().__init__()
		self.deg()

	def f(self, n):
		return n*n+self.a*n+self.b

	def new(self, a, b, unique=True):
		if (self.debug_e):
			print("New called for a= {}, b= {}".format(a, b))
		self.a=a
		self.b=b
		return self.deg(unique)

	def deg(self, unique=True):
		if (self.debug_e):
			print("Degree called for a= {}, b= {}".format(self.a, self.b))
		i=0
		primes=[]
		while (True):
			q=self.f(i)
			if self.isprime(q):
				primes.append(q)
				i+=1
			else: 
				break
		if unique:
			primes2=[]
			for i in primes:
				if not i in primes2:
					primes2.append(i)
			self.pprimes=sorted(primes2)
		else:
			self.pprimes=primes
		return len(self.pprimes)
#
# limit
#

limit=250

#
# basic Euler Polynomial class
#

e=EulerPolynomial(1, 41, False)

#
# we only scan b that are prime because any polynomial with a nonprime b has degree 0
#

tlist=e.until(limit)
blist=[]
for b in tlist:
	blist.append(b)
	blist.append(-b)

print("Produced {} candidates for b. ".format(len(blist)))

result=[]

print(blist)

for b in blist: 

#
# if b is off, we can restrict a to odd numbers, otherwise evem
# this solves the n=1 case because 1+b+a has either to be 2 or odd 
#

	if abs(b)!=2:
		alist=range(-limit+1,limit,2)
	else:
		alist=range(-limit,limit,2)
	for a in alist:
		d=e.new(a, b, False)
		result.append((a, b, d))

print("{} tuples (a,b) analyzed in the range {}".format(len(result), limit))

r10=0
r20=0
r30=0
r40=0

large=[]
for rt in result:
	r=rt[2]
	if r>=10:
		r10+=1
	if r>=20:
		r20+=1
	if r>=30:
		r30+=1
	if r>=40:
		r40+=1
		large.append(rt)

print(" >=10: {}; >=20 {}; >=30 {}; >=40 {} ".format(r10, r20, r30, r40))
print("All large ones:")
print(large)

		

