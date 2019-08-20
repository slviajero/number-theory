from math import sqrt
from primestuff import *

#
# Euler problem inspired
#
# a,b,c being a fermat triple with a<b<c and (*) a+b+c=k=1000
#
# we use the generating equations 
#
# a=n**2-m**2
# b=2mn
# c=n**2+m**2
#
# primitive only if n,m coprime and one of them even the other odd 
# 
# for any give k the equation a+b+c=k yields 
#
# 2n**2+2nm=2*n*(m+n)=k 
#
# this means that solving eulers problem can be reduced to solving
# the diophanian equation k=2*n*(n+m) with the additional condition 
# n>m as we want a>0. Renaming u=k/2 we solve u=n(m+n)
#
# (0) k has to be even
# (1) we use that the maximum n has to be smaller then sqrt(u)
# (2) m<n 
# (3) n must divide u to solve the equation
# (4) n+m must divide u
#

debug=False
if debug:
	primes=Primer(2000)

def eulerf(k):

# condition (0) k must be even, for odd numbers there is no solution

	if odd(k):
		return []

	u=k//2

# condition (1) maximum n is sqrt(k/2) 

	nmax=int(sqrt(u))

# condition (3)
# walk through the range on possible n's 
# and check first if n divides u, create a list of these candidates

	nlist=[]
	for n in range(1,nmax+1):
		if divisible(u,n):
			nlist.append(n)

# check condition (2) and (4) now 
# all possible m must be <n and (n+m) must dived u

	sol=[]
	for n in nlist: 
		for m in range(1,n):
			if divisible(u,n+m):
				sol.append((n,m))


# reduce the list further by asserting that n,m are coprime
# and one of them is even
# this yields only primitive solutions

	sol2=[]
	for t in sol:
		if coprime(t[0], t[1]):
			if even(t[0]) or even(t[1]):
				sol2.append(t)


# sol2 contains now all solutions that satisfy the congruences, 
# and that a>0, and that a,b,c are primitive

# now we construct the actual solutions and make sure that 
# they are scaled to the right k

	sol3=[]
	for s in sol2:
		n=s[0]
		m=s[1]
		a=n**2-m**2
		b=2*n*m
		c=n**2+m**2
		circ=a+b+c
		if (a>b):
			ap=a
			a=b
			b=ap
		f=int(k/circ)
		sol3.append((a*f, b*f, c*f))

	if debug and sol3==[]:
		print(k//2, nmax, nlist)
		print(primes.factor(k//2))
		print(sol3)

	return sol3

def checksolution(t):
	a=t[0]
	b=t[1]
	c=t[2]
	print(a*a+b*b, c*c)
	print(a+b+c)

#
# walk through solutions
#

k=1000
print(eulerf(k))
	

