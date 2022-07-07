import numpy as np
def main(up_to):
	collatz_dict = {}
	for i in range(2, up_to):
		collatz_dict = expand_dict(collatz_dict, i)
	
	largest_chain =  1
	largest_key   = "1"
	for key, value in collatz_dict.items():
		if value > largest_chain:
			largest_key   = key
			largest_chain = value
	return(largest_key, largest_chain)

def find_next(input):
	if 0 == input%2:
		return(input//2)
	return(3*input+1)

def expand_dict(collatz_dict, start):
	lengths, chain = find_chain(collatz_dict, start)
	for length, value in zip(lengths, chain):
		collatz_dict[str(value)] = length
	return(collatz_dict)

def find_chain(collatz_dict, input):
	chain = [input]
	chain_lengths = [1]
	while chain[-1] != 1:
		new = find_next(chain[-1])
		if str(new) in collatz_dict:
			return(add_to_list(chain_lengths, collatz_dict[str(new)]), chain)
		chain_lengths = add_to_list(chain_lengths, 1)
		chain.append(new)
		chain_lengths.append(1)
	return(chain_lengths, chain)

def add_to_list(add_list,value):
	for i, v in enumerate(add_list):
		add_list[i] = v+value
	return(add_list)

if __name__ == "__main__":
	print(main(1000000))