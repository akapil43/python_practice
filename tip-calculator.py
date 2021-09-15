print("Welcome to the Tip Calculator Application.\n\n")
bill_amount=input("What is the bill amount? ₹")
tip_percent=input("\nWhat pwecentage of tip do you want to give. (5, 10, or 15) ")

total_amount_payable = float(bill_amount)+ float(tip_percent)/100*float(bill_amount)

print(f"Total payable amount is: ₹{total_amount_payable}\n")

number_of_persons = input("Enter no. of persons: ") 

amount_per_head = float(total_amount_payable)/float(number_of_persons)

print(f"Each person has to pay: ₹{round(amount_per_head, 2)}")
