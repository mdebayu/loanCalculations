def main():
	principal = 26500;
	print ("Principal = " + str(principal) + "\n");
	monthly_repayment = 444.55;
	print ("Monthly Repayment= " + str(monthly_repayment) +"\n");

	yrly_interest_rate = 5.70;
	years = 5;

	terms  = 12 * years;
	daily_rate_multiplier = (100+yrly_interest_rate/365)/100;




def calculate_interest(balance, termly_interest_rate):
	return balance * termly_interest_rate;

def make_payment(balance,payment):
	return balance - payment;








if __name__ == "__main__":
	main();
