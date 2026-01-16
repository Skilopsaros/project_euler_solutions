
def main(up_to):
	result = {"number":0, "n_digits":0}
	for i in range(1, up_to+1):
		n = find_repeated_digits(i)
		if n > result["n_digits"]:
			result = {"number":i, "n_digits":n}
	return(result)

def find_repeated_digits(i):
	mod = 1 % i
	mods = []
	while mod not in mods:
		mods.append(mod)
		mod = (10*mod)%i
		if not mod:
			return(0)  
	return(len(mods)-mods.index(mod))

if __name__ == "__main__":
	print(main(1000))