def main():
	months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
	months_30 = ["sep", "apr", "jun", "nov"]
	counter = 0
	year = 1901
	weekday = 2
	while year<2001:
		for month in months:
			n_days = 31
			if month == "feb":
				n_days = feb_days(year)
			elif month in months_30:
				n_days = 30
			for day in range(n_days):
				if (day == 0) and (weekday == 7):
					counter += 1
				weekday +=1
				if weekday == 8:
					weekday = 1
		year += 1
	return(counter)


def feb_days(year):
	if year%400 == 0:
		return(29)
	if year%100 == 0:
		return(28)
	if year%4   == 0:
		return(29)
	return(28)

if __name__ == "__main__":
	print(main())