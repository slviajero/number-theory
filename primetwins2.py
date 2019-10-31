from primes import Primer

#
# playing around with pairs again, there are theorems about
# reciprocals that can be tested
#
# the sum of the reciprocals of primes converges to B_2
# the Brun's number which is known from scanning 10**16 pairs 
# to be close to 1.902160583104
#

#
# get primes until 1000 
# these numbers are used to divide the candidates at the second stage of the program
#

base_value=100
debug=False
stage2=True

primer=Primer(base_value)

# stage 1, get the pairs in the first set of numbers
	
pairs=[]
for i in range(0,len(primer)-1):
	if (primer.primes[i+1]-primer.primes[i]) == 2:
		pair=(primer.primes[i], primer.primes[i+1])
		pairs.append(pair)

# stage 2 go beyond base_value using that prime twin pairs need to 
# be of the form 6n-1, 6n+1. As we know the primes up to base value 
# we can now test for primes up to base_value**2

if (stage2):
	for i in range(int(base_value/6), int(base_value**2/6)):
		c1=6*i-1
		c2=6*i+1
		if primer.isprime(c1) and primer.isprime(c2):
			pairs.append((c1, c2))

if debug:
	print(pairs)

#
# the ratio of pairs in the entire range to 1000
#
print("In the interval 2 - {} there are {} pairs".format(base_value**2, len(pairs)))


def b2(p):
	r=0
	for i in range(0,len(p)-1):
		p1=p[i][0]
		p2=p[i+1][1]
		r=r+1/p1+1/p2
	return r

print(b2(pairs))


