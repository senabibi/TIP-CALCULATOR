#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line
bill = int(input("How much money that costs?"))

number_of_people = int(input("How many people that participate ?"))

tip = int(input("How much money do you wanna givve for tips?"))

tips = (100 + tip) / 100

payment = (bill / number_of_people) * tips

print(f"You need to pay {payment:.2f} $.")
