import math

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

# upper bound 

k=4002

if (k%2 != 0):
	print("Diameter not even, no solution. Using Diameter=", k-1)
	k=k-1

u=int(k/2)

# maximum n

#nmax=int(u**(1/2))
nmax=u
print("Maximum n=", nmax)

# walk through the range on possible n's from 
# above and check first if n divides u

nlist=[]

for n in range(nmax,1,-1):
	if (u%n == 0):
		nlist.append(n)

# the possible candidates for n are

print(nlist)

# check the second condition now for (n+m) all possible 
# m must be <n and (n+m) must dived u

sol=[]

for n in nlist: 
	for m in range(n-1,0,-1):
		print("Testing", n,m)
		if ( u%(n+m) == 0):
			sol.append((n,m))

# all solutions that satisfy the conditions of divisibility
# sol will contain more than one tuple even if there is only 
# one solution. Until now we have only tested divisibility 
# and non primitive solutions will appear together with their 
# primitive counterparts, also other noninter multiples seem 
# to appear

print(sol)

for s in sol:
	n=s[0]
	m=s[1]
	a=n**2-m**2
	b=2*n*m
	c=n**2+m**2
	circ=a+b+c
	if (circ == k): 
		print("Solution = ",a,b,c,circ)
	else:
		print("Pseudo solution = ", a,b,c,circ)


# this is still not good
# another test of this
# and yet another after move

