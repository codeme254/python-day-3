#control flow and logical operators
print("Welcome to the rollercoaster")
height = 170
#the if else conditional in python
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry you have to grow taller before you can ride")
# comparison operators >, <, >=, <=, ==, !=
#== means equal to and != means not equal to

# ODD OR EVEN CODING EXERCISE: PROGRAM TO CHECK THAT IF THE NUMBER INPUT VIA THE CONSOLE IS ODD OR EVEN
number = int(input("Which number do you want to check: "))
if number%2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

# Nested if statements and the elif statement
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18: 
        print("Please pay $7.")
    elif age < 22: 
        print("Please pay $9.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride")

# BMI CALCULATOR CHALLENGE
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = round(float(weight)/float(height)**2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, You have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, You are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, You are obese.")
else:
    print(f"Your bmi is {bmi}, You are clinically obese.")

# Pizza order program
print("Welcome to Python pizza deliveries")
size = input("What size pizza do you want? S, M or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N ? ")
extra_cheese = input("Do you want an extra cheese? Y or N? ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Final bill ${bill}")

#multiple if statements in succession
# we can combine multiple conditions
# code challenge leap year exercise
#A year is leap if it is clearly divisible by 4, not clearly divisible by 100 and clearly divisible by 400
year = int(input("Enter the year you want to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year.")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("Not a Leap Year")

# love calculator
print("Welcome to the love calculator")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
full_name = name1+name2
t = full_name.count('t')
r = full_name.count('r')
u = full_name.count('u')
e = full_name.count('e')
true = t + r + u + e
l = full_name.count('l')
o = full_name.count('o')
v = full_name.count('v')
e = full_name.count('e')
love = l + o + v + e
score = int(str(true) + str(love))
if score < 10 or score > 90:
    print(f"Your score is {score} you go together like coke and mentos")
elif score > 40 and score < 50:
    print(f"Your score is {score} you are ok together")
else:
    print(f"Your score is {score}")