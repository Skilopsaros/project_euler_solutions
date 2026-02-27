def main(up_to):
	ps = {0:0}
	for a in range(1,up_to):
		for b in range(a,up_to):
			sqrt = sqrt_if_int(a*a+b*b)
			if not sqrt:
				continue
			p = sqrt + a + b
			if p > up_to:
				break
			if p not in ps:
				ps[p] = 1
			else:
				ps[p] += 1
	max_multiplicity_p = 0
	for p, m in ps.items():
		if m > ps[max_multiplicity_p]:
			max_multiplicity_p = p
	return(max_multiplicity_p)


def sqrt_if_int(n):
	sqrt = int(pow(n, 0.5))
	if sqrt*sqrt == n:
		return(sqrt)
	return(False)

if __name__ == "__main__":
	print(main(1000))

# def sqrt_if_int(n, guess=None):
# 	if n == 1:
# 		return(1)
# 	if not guess:
# 		guess = n//2
# 	if guess == 0 or guess == 1:
# 		return(False)
# 	squared_guess = guess*guess
# 	if squared_guess == n:
# 		return(guess)
# 	low_bound = n//guess
# 	new_guess = (low_bound+guess)//2
# 	if new_guess == guess:
# 		return(False)
# 	if abs(new_guess - guess) == 1 and new_guess*new_guess != n:
# 		return(False) 
# 	return(sqrt_if_int(n,new_guess))