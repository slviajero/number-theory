from primes import Primer

#
# test dynamic factorization and solve the 
# problem 3 
#

number=600851475143
p=Primer()
f=p.factor(number)
print("Factors of {} are {} ".format(number, f))
print("Last prime in the list is {} ".format(f[-1]))
