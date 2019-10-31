from math import sqrt, factorial

#
# euklids algorithm to find the greatest common divisor of two integers
# non recursive for a change
# no optimization like for example handling situation where one factor is 
# much bigger than the other
#
def euklid(i,j):
	if (i<1 or j<1):
		return 0
	while (i!=j):
		if (i>j):
			i=i-j
		else:
			j=j-i
	return j

def euklid2(i,j):
	q=max(i,j)
	p=min(i,j)
	r=q%p
	if (r==0):
		return p
	else:
		return euklid(r,p)

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
# Naive binomial
#

def binomial(n, m):

	if (n<0):
		return 0
	if (m>n):
		return 0

	return factorial(n) // factorial(m) // factorial(n - m)

def binomial2(n, m):

	if (n<0) or (m<0):
		return 0
	if (m>n):
		return 0

	numerator=1
	demoninator=1
	for k in range(1,m+1):
		numerator=numerator*(n-k+1)
		demoninator=demoninator*k

	return numerator//demoninator


if __name__=="__main__":

	d=euklid(187, 123)
	print("Greatest common divisor of {} and {} is {}".format(187, 123, d))

	if coprime(187,123):
		print("187 and 123 are coprime")

	d=euklid(11, 121)
	print("Greatest common divisor of {} and {} is {}".format(11, 121, d))

	a=12*8
	b=12*8*3
	d=euklid(a, b)
	e=euklid2(a, b)
	print("Greatest common divisor of {} and {} is {} or {}".format(a, b, d, e ))

	if not coprime(11,121):
		print("11 and 121 are not coprime")

	print("Binomial (10, 5) is {}".format(binomial(10,5)))
	a=10
	b=9
	print("Binomial ({}, {}) is {}".format(a, b, binomial2(a,b)))	


