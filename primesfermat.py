# solves the problem of finding all possible a,c that solve 
# a**2 + b**2 = c**2 for a given b
#
# method is to rewrite the equation as c**2 - a**2 = (c-a)(c+a) = b**2
# from here one can find the prime factors of b and distribute them in all possible ways to generate the 
# two integers (c-a) and (c+a) 
# then one solves for c and a. 
#
# this was just a playground to to combinatorics with all kind of data structures in python 

# static for now
primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

# factorize an integer n
def factor(n):
	f=[]	
	for prime in primes:
		if n <= 1:
			return f
		while (n % prime == 0):
			n = int(n / prime)
			f.append(prime)
	if ( n > 1):
		f.append(n)
	return f

# order (=number of factors in the second part) of the tuple
def tupleorder(tuple):
	return len(tuple[1])

# equality of tuples
def sametuple(t1, t2):
	return (t1[0] == t2[0]) & (t1[1] == t2[1])
		
# expand one tuple one step further to create a list of possibilites by shifting one factor left
def expandtuple(tuple):
	first=tuple[0]
	second=tuple[1]
	p=[]
	for f in second:
		l2=second[:]
		l1=first[:]
		l2.remove(f)
		l1.append(f)
		l1.sort()
		p.append((l1, l2)) 		 			 			 
	return p

# reduce list of tuples removing doubles
def reducetuple(list):
	l1=list[:]
	l2=[]
	n=len(l1)
	for i in range(0,n):
		for j in range(i+1,n):
			if sametuple(l1[i],l1[j]):
				l1[j]=(0,0)	
	for t in l1:
		if t != (0,0):
			l2.append(t)
	return l2

# expand a list of tuples and generate a new larger list of tuples
# take the list and expand each element to a new list, combine and reduce them
def expandlistonce(l):
	l1=[]
	if tupleorder(l[0]) == 1:
		return l1
	for t in l:
		l2=expandtuple(t)
		for t2 in l2:
			l1.append(t2)
	return reducetuple(l1)

# order of the list is the order of the shortest tuple
def listorder(l):
	lasttuple=l[-1]
	return tupleorder(lasttuple)

# expand a list fully until order of the step is one, normally invoked with a list of just one element, recursive
def expandlist(list):
	l1=[]
	l2=[]
	if listorder(list)==1:
		return list
	l1=expandlistonce(list)
	l2=expandlist(l1)
	return list+l1+l2

# corrects for the last solution which is the first reverse
def completelist(list):
		l1=list[0][0]
		l2=list[0][1]
		list.append((l2,l1))

# multiply all elements of a list
def multiplylist(list):
	n=1
	for i in list:
		n=n*i
	return n

# create the list of alpha and beta from the prime factors in the tuples
def multiplytuples(list):
	p=[]
	for t in list:
		t1=(multiplylist(t[0]), multiplylist(t[1]))
		p.append(t1)
	return p

# creates the three numbers xyz of the pythagorean triangle, we discard the trivial, negative and multiples of 1/2
def calculatexyz(list):
	print(len(list))
	p=[]
	for t in list:
		if (t[0]+t[1]) % 2 == 0:
			x=int((t[0]-t[1])/2)
			z=int((t[0]+t[1])/2)
			if x>0:
				p.append((x, y, z))
	print(len(p))
	return p
	
	
# main program 


y=3*7*11
factors=factor(y)
print(factors)

factors2=[]
for f in factors:
	factors2.append(f)
	factors2.append(f)
	

inittuple=([1], factors2[:])
initiallist=[inittuple]

l=expandlist(initiallist)
completelist(l)
l=reducetuple(l)

r=multiplytuples(l)
s=calculatexyz(r)	

print(s)
		

