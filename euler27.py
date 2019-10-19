from primes import Primer

class EulerPolynomial:

	def __init__(self, p, a=1, b=41):
		self.a=a
		self.b=b
		self.p=p
		self.primes=[]

	def f(self, n):
		return n*n+self.a*n+self.b

	def new(self, a, b):
		self.a=a
		self.b=b

	def deg(self, unique=True):
		i=0
		primes=[]
		while (True):
			q=self.f(i)
			if self.p.isprime(q):
				primes.append(q)
				i+=1
			else: 
				break
		if unique:
			primes2=[]
			for i in primes:
				if not i in primes2:
					primes2.append(i)
			self.primes=sorted(primes2)
		else:
			self.primes=primes
		return len(self.primes)
#
# limit
#
limit=2000
#
# The primer - does all the prime stuff
#
primer=Primer()

#
# basic Euler Polynomial class
#

e=EulerPolynomial(primer)

#
# we only scan b that are prime because any polynomial with a nonprime b has degree 0
#
tlist=primer.until(limit)
blist=[]
for b in tlist:
	blist.append(b)
	blist.append(-b)

print("Produced {} candidates for b. ".format(len(blist)))

result=[]

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
		e.new(a, b)
		d=e.deg(False)
		result.append((a, b, d))

print(len(result))

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

print(r10, r20, r30, r40)
print(large)

for l in large:
	print(l, primer.coprime(l[0], l[1]))


		

