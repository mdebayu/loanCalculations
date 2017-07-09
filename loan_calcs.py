def main():
	principal = 26500;
	print ("Principal = " + str(principal) + "\n");
	monthly_repayment = 444.55;
	print ("Monthly Repayment= " + str(monthly_repayment) +"\n");

	_yrly_interest_rate = 5.70;
	years = 5;

	terms  = 12 * years;
	daily_rate_multiplier = get_daily_rate (_yrly_interest_rate)


def get_daily_rate(_rate):
    return (100+_rate/12)/100;

def calculate_interest(balance, termly_interest_rate):
	return balance * termly_interest_rate;

def make_payment(balance,payment):
	return balance - payment;

def calculate_monthly_repayment(balance, rate, terms, balloon_payment):
    assert(rate>1);
    return((balance*(rate**terms)-balloon_payment) * (rate-1 ))/(rate**(terms-1)-1)






if __name__ == "__main__":
    p=calculate_monthly_repayment(26500,get_daily_rate(5.7),60,5300)
    print p;


#main();
