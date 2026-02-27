from common import functions as cf

def main(bellow):
	primes = cf.find_primes(bellow)
	successful_series = []
	for i, p in enumerate(primes):
		if i == len(primes) - 1:
			continue
		j = i+1
		series = [p, primes[j]]
		s = sum(series)
		while s < bellow:
			if s in primes:
				successful_series.append(list(series))
			j += 1
			series.append(primes[j])
			s += primes[j]
	successful_series.sort(key=len,reverse=True)
	return(sum(successful_series[0]))




if __name__ == "__main__":
	print(main(1000000))
