import math as maths

def main(input, start = 2):
	check_number = input
	for i in range(start, int(input/2+1)):
		if is_prime(i):
			div, mod = divmod(check_number, i)
			if 0 == mod:
				print(f"{i}, {div}")
				if is_prime(div):
					return(int(div))
				return(main(div, i))

def is_prime(n):
	for i in range(2,maths.floor(pow(n,0.5))+1):
		if n%i==0:
			return(False)
	return(True)

if __name__ == "__main__":
	print(main(600851475143))