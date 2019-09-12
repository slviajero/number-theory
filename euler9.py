from math import sqrt
import argparse
from time import perf_counter 

#
# get and process the command line arguments
#

ap = argparse.ArgumentParser()
ap.add_argument("-k", "--sum", required=False, default=1000, 
	help="sum a+b+c")
ap.add_argument("-r", "--range", required=False, default=0, 
	help="range of values to be checked after k")
ap.add_argument("-e", "--explain", required=False, default=False, action="store_true",
	help="explain the solution")
ap.add_argument("-m", "--math", required=False, default=False, action="store_true",
	help="explain the math")
ap.add_argument("-t", "--time", required=False, default=False, action="store_true",
	help="measure execution time")

args = vars(ap.parse_args())

k=int(args['sum'])
explain=args['explain']
math=args['math']
measure_time=args['time']
r=int(args['range'])

#
# explainers - function that explain the result if desired
#

def explain_math():
	explaintext=\
"Problem statement:\n"\
" a,b,c being a fermat triple with a<b<c and (*) a+b+c=k\n"\
" (k=1000 in the original problem, this programs solves for any k)\n"\
"Solution method:\n"\
" all primitive triples can be generated my the equations\n"\
"     a=n**2-m**2, b=2*m*n, c=n**2+m**2\n"\
"     (n,m coprime and one of them even the other odd)\n"\
" nonprimitive triples can be generated by multiplying a primitive\n"\
" triples with with a factor f\n"\
"\n"\
" for any give k the equation a+b+c=k yields\n"\
"     2*n*(m+n)*f=k  (f is a factor if the triple is nonprimitive)\n"\
" solving the problem can be reduced to solving the diophanian\n"\
"        k=2*n*(n+m)*f                                        \n"\
"  with the additional condition n>m as we want a>0.          \n"\
"\n"\
" This equation only has a solution under the following conditions\n"\
" (0) k has to be even                                            \n"\
" (1) the maximum n has to be smaller then sqrt(k/2)              \n"\
" (2) n must divide k to solve the equation                       \n"\
" (3) m<n (as a has to be positive)                               \n"\
" (4) n+m must divide k                                           \n"\
" (5) n, m have to be coprime and one has to be even              \n"\
" The program filters n,m for these conditions and then calulates f "
	return explaintext

def explain_condition0():
	explaintext=\
	"------------------------------------------------------\n"\
	"Condition 0: The input has to be even for a solution  \n"\
	"------------------------------------------------------"
	return explaintext

def explain_condition1(nmax):
	explaintext=\
	"Condition 1: the maximum n is given by k/2>n^2       \n"\
	"This means that we only have to check until n= {}    \n"\
	"------------------------------------------------------".format(nmax)
	return explaintext

def explain_condition2(nlist):
	explaintext=\
	"Condition 2: n has to divide k for a solution        \n"\
	"This means that we only have to check n = {}     \n"\
	"------------------------------------------------------".format(nlist)
	return explaintext

def explain_condition3and4(nmlist):
	explaintext=\
	"Condition 3+4: m has to be smaller than n and   \n"\
	"n+m has to divide k. This leads to the candidates (n,m) = {} \n"\
	"------------------------------------------------------".format(nmlist)
	return explaintext

def explain_condition5(nmlist):
	explaintext=\
	"Condition 5: m, n have to be coprime and one of them   \n"\
	"Has to be even. The remaining solutions are (n,m) = {} \n"\
	"------------------------------------------------------".format(nmlist)
	return explaintext

def explain_solution(s, a, b, c, f):
	explaintext=\
	"Pair (n,m) {} \n"\
	"Leads to the primitive triple {} \n"\
	"Multiplying by {} \n"\
	"Leads to the solution {} \n".format(s, (a, b, c), f, (a*f, b*f, c*f))
	return explaintext

#
# number theory helper functions
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
# the algorithm, see explain_math for documentation
#

def eulerf(k):

# explain the math if desired

	if math:
		print(explain_math())
		
# condition (0) k must be even, for odd numbers there is no solution

	if odd(k):
		if explain:
			print(explain_condition0())
		return []

	u=k//2

# condition (1) maximum n is sqrt(k/2) 

	nmax=int(sqrt(u))
	if explain:
		print(explain_condition1(nmax))

# condition (2)
# walk through the range on possible n's 
# and check first if n divides u, create a list of these candidates

	nlist=[]
	for n in range(1,nmax+1):
		if divisible(u,n):
			nlist.append(n)

	if explain: 
		print(explain_condition2(nlist))

# check condition (3) and (4) now 
# all possible m must be <n and (n+m) must dived u

	sol=[]
	for n in nlist: 
		for m in range(1,n):
			if divisible(u,n+m):
				sol.append((n,m))

	if explain: 
		print(explain_condition3and4(sol))

# reduce the list further by asserting that n,m are coprime
# and one of them is even
# this yields only primitive solutions

	sol2=[]
	for t in sol:
		if coprime(t[0], t[1]):
			if even(t[0]) or even(t[1]):
				sol2.append(t)

	if explain: 
		print(explain_condition5(sol2))

# sol2 contains now all solutions that satisfy the congruences, 
# that a>0, and that a,b,c are primitive
# now we construct the actual solutions and make sure that 
# they are scaled to the right k

	sol3=[]
	for s in sol2:
		n,m=s
		a=n**2-m**2
		b=2*n*m
		c=n**2+m**2
		circ=a+b+c
		if (a>b):
			ap=a
			a=b
			b=ap
		f=k//circ
		if explain: 
			print(explain_solution(s, a, b, c, f))
		sol3.append((a*f, b*f, c*f))

	return sol3

#
# calculate and measure the execution time
#

if r==0:
	# calculate just one value
	cl=perf_counter()
	result=eulerf(k)
	cl=perf_counter()-cl
	print(k, result)
else:
	cl=perf_counter()
	results=[]
	for i in range(k,k+r):
		results.append((i,eulerf(i)))
	cl=perf_counter()-cl	
	for result in results:
		if result[1]!=[]:
			print(result[0], result[1])

if (measure_time):
	print("Execution time {} microseconds".format(int((cl)*1000000))) 