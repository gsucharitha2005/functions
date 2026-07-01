def check_admission_eligibility(age,location):
	if age>=10 and age<=12 and location=="rural":
		return True
	else:
		return False
print(check_admission_eligibility(11,"rural"))
print(check_admission_eligibility(10,"urban"))