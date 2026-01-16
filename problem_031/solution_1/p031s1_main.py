import copy

def main(values, total):
	all_combinations = find_all_combinations(values, total)
	return(len(all_combinations))

def find_all_combinations(values, total, coins_used = []):
	all_combinations = []
	for value in values:
		if (not coins_used) or value <= coins_used[-1]:
			new_coins_used = coins_used + [value]
			if sum(new_coins_used) == total:
				all_combinations.append(new_coins_used)
			elif sum(new_coins_used) < total:
				all_combinations.extend(find_all_combinations(values, total, new_coins_used))
	return(all_combinations)

		
if __name__ == "__main__":
	values = [1, 2, 5, 10, 20, 50, 100]
	print(main(values, 200)+1)