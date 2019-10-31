from primes import Primer
from math import log

#
# Solving the Euler problem 127
#

primer=Primer()


def newton(n0, steps):
	a=(10**10)/2
	n=n0
	for i in range(0,steps):
		f=n*n*(log(n)+log(log(n))-1.0)-a
		fp=2*n*(log(n)+log(log(n))-1.0)+n*(1+1/log(n))
		n=n0-f/fp
		n0=n
	return n


#
# solving the equation 
# ((p+1)**n+(p-1)**n)%p**2 = 2*p*n for n off and 2 for n even
#
def res(p, n):
	if primer.even(n):
		return 2
	else:
		return 2*p*n
#
# calculate the residue using the value of the nth prime 
# from the asypmtotic formula in primer
#
def resest(n):
	p=int(primer.p(n))
	return res(p,n)

#
# estimate when the residue is greater 10**10
#
def estimaten(start, debug=False):
	if primer.odd(start):
		n=start
	else:
		n=start+1
	r=resest(n)
	while r<10**10:
		n+=1000
		r=resest(n)
		if debug:
			print(n,r)
	return n-1000

#
# generate primes until we are done
#
def primeit(n, debug=False):
	primer.getprimes2(n)
	while True:
		n=len(primer)
		p=primer.prime(n)
		r=res(p,n)
		if r<10**10:
			primer.next()
		else:
			if debug:
				print(n, p, r)
			break
	return n

print("Newton estimate of the simple formula {}".format(newton(7800,6)))
e=estimaten(7800)
print("First estimation of the value: {}".format(e))
n=primeit(e)
print("Exact result: {}".format(n))
print("Prime is: {}".format(primer.prime(n)))
print("Estimated prime value is: {}".format(int(primer.p(n))))





