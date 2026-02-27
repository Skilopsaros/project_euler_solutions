def main():
	pn = [get_nth_pentagonal_number(n) for n in range(1,4)]
	i = 0
	while True:
		i+=1
		for j in range(i):
			while (pn[i]+pn[j] > pn[-1]):
				extend_pentagonal_numbers(pn)
			if pn[i]+pn[j] in pn and pn[i]-pn[j] in pn:
				return(pn[i] - pn[j])
	
	
def extend_pentagonal_numbers(pentagonal_numbers):
	pentagonal_numbers.append(get_nth_pentagonal_number(len(pentagonal_numbers)+1))

def get_nth_pentagonal_number(n):
	return(n*(3*n-1)//2)

if __name__ == "__main__":
	print(main())
