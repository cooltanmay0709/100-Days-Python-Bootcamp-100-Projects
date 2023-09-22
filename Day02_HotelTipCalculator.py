#1 Create a greeting for your program.
#2 Ask the user for total hotel bill.
#3 Ask the user for the percentage of tip he/she would like to give. 10, 12 or 15.
#4 Ask the user for number of people to split the bill.
#5 Calculate the total amount each person should pay after adding a tip to the bill and splitting it.
#5 Make sure the input cursor shows on a new line.
# Github Link - 

print("Welcome to the Hotel Tip Calculator !!!")
bill = float(input("What was the total bill? "))
percentTip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
personSplit = int(input("How many people to split the bill? "))

totalTip = float(bill*percentTip/100)
totalBill = float(totalTip + bill)
personPay = float(totalBill/personSplit)

print(f"Total bill after adding tip: {totalBill}\nEach person should pay: INR {personPay}")