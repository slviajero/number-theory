from primes2 import Primer

p=Primer(600, debug=False)

print(p.list())
print("Number of primes: ", p.len())
print("Maximum prime: ", p.max())

l=[]
for i in range(1234959513,1234959513+100):
	l.append(len(p.factor(i)))


print(l)
print("Number of primes: ", p.len())

l2=[]
fact=p.getfactorizer(1)
for i in range(1234959513,1234959513+100):
	fact.init(i)
	t=0
	for f in fact:
		t+=1
	l2.append(t)

print(l2)

l3=[]
for i in range(1234959513,1234959513+100):
	fact.init(i)
	l3.append(len(fact))

print(l3)

fact2=p.getfactorizer(187)
for f in fact2:
	continue

print(fact2.factors)
next(fact2)
print(fact2.factors)





