#
# playing around with pairs again, there are theorems about
# reciprocals that can be tested
#

#
# get primes until 1000
#
base_value=1000
primes=[2]
for number in range(3,base_value):
	is_prime=True
	for p in primes:
		if number % p == 0:
			is_prime=False
			break
	if is_prime:
		primes.append(number)

#
# get prime number pairs
#
	
pairs=[]
for i in range(0,len(primes)-1):
	if (primes[i+1]-primes[i]) == 2:
		pair=(primes[i], primes[i+1])
		pairs.append(pair)

#
# the ratio of pairs in the entire range to 1000
#
print("Number of pairs in the interval", base_value, len(pairs)/base_value)

#
# generate the distances, the reciprocals and the sum of them
#

distances=[]
average_distances=[]
sum_of_distance=0
sum_of_reci=0
for i in range(0,len(pairs)-1):
	pair1=pairs[i]
	pair2=pairs[i+1]
	distance=pair2[0]-pair1[0]
	reci=1/pair1[0]+1/pair1[1]
	distances.append(distance)
	sum_of_distance=distance+sum_of_distance
	sum_of_reci=reci+sum_of_reci
	print("The sum of the reciprocals of pairs in the range", i, sum_of_reci)
	average_distances.append(sum_of_distance/(i+1))

#
# unfinished work, things to come
#


