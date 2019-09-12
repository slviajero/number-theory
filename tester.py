from primes import Primer

p=Primer(600, debug=False)

print(p.list())
print("Number of primes: ", p.len())
print("Maximum prime: ", p.max())

l=[]
for i in range(1234959513,1234959513+100):
	l.append(len(p.factor(i)))


print(l)
print("Number of primes: ", p.len())
