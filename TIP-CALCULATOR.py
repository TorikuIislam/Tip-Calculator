print("Welcome to the tip calculator.")
bill=float(input(" What was the total bill? $ \n"))
tip=int(input( "What percentage tip would you like to give ? 10 , 12 , or 15 ?\n"))
people=int(input("How mant people to split the bill ?\n"))

tip_percentage=tip/100
bill_percentage=tip_percentage*bill
total_bill=bill+bill_percentage

people_give=round(total_bill/people,2)

print(f"Each person Sholu Pay : ${people_give}\n")

