from primes import Primer

#
# Playing around with the Riemand zeta function 
#

primer=Primer(1900)
print("Number of primes:", len(primer))

# the zeta function for s real and s>1 summing up the integers
sum=10000
print("Summation limit:", sum)

def zeta_n(s):
	z=0.0
	for i in range(1,sum):
		z=z+(1/i)**s
	return z
	
# the zeta function for s real and s>1 summing up primes 
	
def zeta_p(s):
	z=1.0
	for p in primer:
		z=z/(1-p**(-s))
	return z

# a few well known values of zeta

zeta2=3.14159265359**2/6
dn=zeta_n(2)-zeta2
dp=zeta_p(2)-zeta2
print("Zeta of 2 is {} ".format(zeta2))
print("Delta of z_n(2) is {} ".format(dn)) 
print("Delta of z_p(2) is {} ".format(dp))

zeta32=2.6123753486
dp=zeta_p(3/2)-zeta32
dn=zeta_n(3/2)-zeta32

print("Zeta of 3/2 is {} ".format(zeta32))
print("Delta of z_n(2) is {} ".format(dn)) 
print("Delta of z_p(2) is {} ".format(dp))
