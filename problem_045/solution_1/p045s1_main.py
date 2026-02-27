def main():
	t = 286
	p = 168
	pentagonal_number = get_nth_pentagonal_number(p)
	h = 145
	hexagonal_number = get_nth_hexagonal_number(h)
	while True:
		t += 1
		triangle_number = get_nth_triangle_number(t)
		while triangle_number > pentagonal_number:
			p += 1
			pentagonal_number = get_nth_pentagonal_number(p)
		while triangle_number > hexagonal_number:
			h+=1
			hexagonal_number = get_nth_hexagonal_number(h)
		if triangle_number == hexagonal_number and triangle_number == pentagonal_number:
			print(t, p, h)
			return(triangle_number)
	
def get_nth_triangle_number(n):
	return(n*(n+1)//2)

def get_nth_pentagonal_number(n):
	return(n*(3*n-1)//2)

def get_nth_hexagonal_number(n):
	return(n*(2*n-1))

if __name__ == "__main__":
	print(main())
