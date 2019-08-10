class Fraction():

	def __init__(self, numerator=0, denominator=1):
		if denominator == 0:
			print("Error denominator 0")
			exit()		
		self.numerator=numerator
		self.denominator=denominator
		self.cutshort()

	def display(self):
		print(self.numerator)
		print(self.denominator)


	def multiply(self, bruch):
		n=self.numerator*bruch.numerator
		m=self.denominator*bruch.numerator
		b=Fraction(n,m)
		b.cutshort()
		return b

	def euclid(self):
		n=abs(self.numerator)
		m=abs(self.denominator)

		if n == 0:
			return 1
		while True:
			if n>m:
				n=n-m
			elif n<m:
				m=m-n
			else:
				break
		return n

	def cutshort(self):
		g=self.euclid()
		self.numerator=self.numerator//g
		self.denominator=self.denominator//g

	def inverse(self):
		if self.numerator != 0:
			n=self.numerator
			self.numerator=self.denominator
			self.denominator=n
		else:
			print("Error denominator 0")
			exit()

	def add(self, bruch):
		n=self.numerator*bruch.denominator+self.denominator*bruch.numerator
		m=self.denominator*bruch.denominator
		b=Fraction(n,m)
		b.cutshort()
		return b

	def negate(self):
		self.numerator=-self.numerator
