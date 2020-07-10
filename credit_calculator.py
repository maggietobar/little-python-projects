import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type", type = str, help = 'Indicates the type of payments: "annuity" or "diff"')
parser.add_argument("--payment", type = int, help = "Amount of monthly payment.")
parser.add_argument("--principal", type = int, help = "Capital amount.")
parser.add_argument("--periods", type = int, help = "Number of months and/or years needed to repay the credit.")
parser.add_argument("--interest", type = float, help = "Interest rated expressed in decimals.")
args = parser.parse_args()

if args.type not in ("annuity", "diff"):
    print('Incorrect parameters')
elif args.type == "diff" and args.payment is not None:
    print('Incorrect parameters')
elif len(sys.argv) < 4:
    print('Incorrect parameters')
elif args.interest is None:
    print('Incorrect parameters')
elif ((args.payment is not None and args.payment < 0) or (args.principal is not None and args.principal < 0) or (args.periods is not None and args.periods < 0 ) or (args.interest is not None and args.interest < 0)):
    print('Incorrect parameters')
else:
    nominal_interest = args.interest / (100 * 12)
    if args.type == "diff":
        total_payment = 0
        for month in range(1, args.periods + 1):
            payment = (args.principal / args.periods) + nominal_interest * (args.principal - (args.principal * (month - 1) / args.periods))
            print("Month ", month, ": paid out ", math.ceil(payment))
            total_payment += math.ceil(payment)
        print("Overpayment = ", total_payment - args.principal)
    elif args.type == "annuity":
        if args.periods is None:
            periods_count = math.log((args.payment / (args.payment - nominal_interest * args.principal)), (1 + nominal_interest))
            if round(periods_count) > 12:
                if round(periods_count) % 12 != 0:
                    print("You need ", math.floor(periods_count/12)," years and ", math.ceil(periods_count % 12),"months to repay this credit!")
                    print("Overpayment = ", (args.payment *  round(periods_count)) - args.principal)
                elif round(periods_count) % 12 == 0:
                    print("You need ", round(periods_count/12)," years to repay this credit!")
                    print("Overpayment = ", (args.payment *  round(periods_count)) - args.principal)
            elif round(periods_count) < 12:
                if periods_count < 1:
                    print("You need one month to repay this credit!")
                    print("Overpayment = ", (args.payment *  round(periods_count)) - args.principal)
                else:
                    print("You need ", math.ceil(periods_count)," months to repay this credit!")
                    print("Overpayment = ", (args.payment *  math.ceil(periods_count)) - args.principal)
            elif round(periods_count) == 12:
                print("You need one year to repay this credit!")
                print("Overpayment = ", (args.payment *  round(periods_count)) - args.principal)
            
        elif args.payment is None:
            annuity_payment = args.principal * (nominal_interest * math.pow((1 + nominal_interest), args.periods))/ (math.pow((1 + nominal_interest), args.periods) - 1)
            print("Your annuity payment = ", math.ceil(annuity_payment), "!")
            print("Overpayment = ", (math.ceil(annuity_payment) *  args.periods) - args.principal)
                
        elif args.principal is None:
            credit_principal = args.payment / ((nominal_interest * math.pow((1 + nominal_interest), args.periods))/ (math.pow((1 + nominal_interest), args.periods) - 1))
            print("Your credit principal = ", math.floor(credit_principal), "!")
            print("Overpayment = ", (args.payment *  args.periods) - math.floor(credit_principal))

            
        
