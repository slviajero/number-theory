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
# 2n**2+2nm=k 
#
# all n that satisfy this equation need to be smaller than sqrt(k/2) 


# a very elementary euklid algorithm 

def euklid(i,j):
	if ((i==1) or (j==1)):
		return 1;
	if (j==i):
		return j;
	if (j>i):
		return euklid(j-i,i)
	else: 
		return euklid(i-j,j)

# upper bound  
k=1000

# maximal n
nmax=int((k/2)**(1/2))

# print("Maximum n is", nmax);

# the tuples, triples, primitives and circumferences

tuples=[]
triples=[]
primitives=[]
circ=[]

# contructing all relevant tuples (n,m)

for n in range(1,nmax+1):
	mmax=int(k/(2*n)-n);
	# print("mmax ", n , mmax)
	for m in range(1,mmax+1):
		tuples.append((n,m))

print(tuples)

# finding all the a,b,c and reducing the list to the primitive ones

for t in tuples:
	n=t[0]
	m=t[1]
	if (n>m):
		a=n**2-m**2
		b=2*m*n
		c=n**2+m**2
		u=a+b+c
		if (a<b):
			triples.append((a,b,c,u))
		else:
			triples.append((b,a,c,u))
		if (euklid(n,m)==1 and (((m%2)==0) or ((n%2)==0))):
			circ.append(u)
			if (a<b):
				primitives.append((a,b,c))
			else:
				primitives.append((b,a,c))

# isolating the ones that are slightly above 
# as the upper bound is not exact for (n,m)

def countuntil(uu):
	z=0;
	for t in triples:
		if (t[3]<=uu): 
			z=z+1
	return z;

print("Uper Bound", k)
print("Number of triples", len(triples))
print("Number of primitives", len(circ))
# print(len(primitives))
print(circ)
#print(primitives)
#print(triples)





