def main():
	ph = PentagonalHelper()
	n = 2
	while True:
		pn = ph.get_p(n)
		m = n+2
		while ph.get_p(m)-ph.get_p(m-1)<=pn:
			m+=1
		for i in range(1,m):
			pi = ph.get_p(i)
			instabreak = False
			first_iteration = True
			for j in range(i+1, m+1):
				pj = ph.get_p(j)
				if (pj - pi) == pn:
					if ph.is_pentagonal(pj + pi):
						return(pj, pi)
				elif (pj - pi) > pn:
					if first_iteration:
						instabreak = True
					break
				first_iteration = False
			if instabreak:
				break
		n+=1
		if n%100 == 0:
			print(n, pn)

class PentagonalHelper:
	def __init__(self):
		self.p = [1,5]
		self.p_set = {1,5}
	
	def is_pentagonal(self,n):
		while n > self.p[-1]:
			self.extend_pentagonal_numbers()
		return(n in self.p_set)
		
	def extend_pentagonal_numbers(self,n=1):
		for i in range(n):
			new_number = self.p[-1]+3*(len(self.p)+1)-2
			self.p.append(new_number)
			self.p_set.add(new_number)
	
	def get_p(self,n):
		if n >= len(self.p)-1:
			self.extend_pentagonal_numbers(n-len(self.p)+1)
		return(self.p[n])

	

if __name__ == "__main__":
	print(main())
