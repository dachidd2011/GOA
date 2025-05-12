# 2) კომენტარებით ახსენით რა არის sequences, iteration და selection. მოიყვანეთ მათი მაგალითები

# 3) კომენტარებით ახსენით, რა არის ალგორითმი და ჩამოთვალეთ რა გზები არსებობს მის წარმოსადგენად.

# 4) შეეცადეთ თქვენით მიხვდეთ, თუ რა პასუხს გამოიტანს შემდეგი კოდი:

# print(True or False and False or True and False or False and False or False and True and False or True)
# print(5 > 10 or 7 * 7 / 7 == 7 and False or True and "1234" != "1234" and 7 + 3 * 3 + 1 == 15 and True and True or 100 > 100 or True)

# პირველ რიგში დაუყევით and ლოგიკურ ოპერატორებს, შემდეგ კი დარჩენილ or ოპერატორებს

# 5) მომხმარებელს შემოატანინეთ რიცხვი და თუ ის არის ლუწი და არის 10-ზე მეტი, ან ტოლია 7-ის, დაბეჭდეთ True

# 6) ივარჯიშეთ შემდეგ ფუნქციებზე: int, str, float, bool. თითოეულზე გააკეთეთ 3-3 მაგალითი

# 7) მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ, თუ ის არის ნაკიანი დაბეჭდეთ "This is leap year".(ნაკიანი წელიწადი იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე)
# ________________________________________________________________________________________________

# 2) კომენტარებით ახსენით რა არის sequences, iteration და selection. მოიყვანეთ მათი მაგალითები

# "sequences":
# A sequence is the order in which instructions are executed, one after another. The code runs in a top-down, step-by-step,as written.
# example:

# 1. Ask the user for their name
name = input("Enter your name: ")

# 2. Print a greeting
print("Hello,", name)

# 3. Say goodbye
print("Goodbye")


# "iteration":
# Iteration means repeating a set of instructions. This can be done using loops like "for" or "while".
# example:

# A "for" loop that prints "Hello!" five times
for i in range(5):
    print("Hello!", i)


# "selection":
# Selection is used to make decisions in code. It allows different blocks of code to run depending on conditions, using if, elif, and else.
# example:
# Ask the user for their age
age = int(input("Enter your age: "))

# Check the condition
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

#________________________________________________________________________________________

# 3) კომენტარებით ახსენით, რა არის ალგორითმი და ჩამოთვალეთ რა გზები არსებობს მის წარმოსადგენად.

# "algorithm"
# An algorithm is a clear, step-by-step set of instructions designed to solve a specific problem or perform a task.
# In programming, it's the logic or process that a computer follows to get the desired result.

# ways to represent algorithm:
# 1. Plain Text Description:
# Written in natural language, step by step.

# 2. Pseudocode
# Looks like code, but written in a human-readable way without strict syntax.

# 3. Flowchart
# A visual diagram using shapes (e.g., ovals for Start/End, rectangles for actions, diamonds for decisions).

# 4. Programming Code
# The algorithm written in a real programming language like Python, Java, etc.

#_________________________________________________________________________________

# 4) შეეცადეთ თქვენით მიხვდეთ, თუ რა პასუხს გამოიტანს შემდეგი კოდი:
# print(True or False and False or True and False or False and False or False and True and False or True)... output=True
# print(5 > 10 or 7 * 7 / 7 == 7 and False or True and "1234" != "1234" and 7 + 3 * 3 + 1 == 15 and True and True or 100 > 100 or True)... output=True

#______________________________________________________________________________________

# პირველ რიგში დაუყევით and ლოგიკურ ოპერატორებს, შემდეგ კი დარჩენილ or ოპერატორებს
#noting yet













# 5) მომხმარებელს შემოატანინეთ რიცხვი და თუ ის არის ლუწი და არის 10-ზე მეტი, ან ტოლია 7-ის, დაბეჭდეთ True

# Ask the user to input a number
number = int(input("Enter a number: "))

# Check if the number is even and greater than 10, or if it's equal to 7
if (number % 2 == 0 and number > 10) or number == 7:
    print(True)
else:
    print(False)

#_________________________________________________________________________________

# 6) ივარჯიშეთ შემდეგ ფუნქციებზე: int, str, float, bool. თითოეულზე გააკეთეთ 3-3 მაგალითი

#int()
# example:
# Example 1: Converting a string to an integer
num = int("10")
print(num)  # Output: 10

# Example 2: Converting a float to an integer
num = int(3.14)
print(num)  # Output: 3

# Example 3: Converting a negative string to an integer
num = int("-5")
print(num)  # Output: -5

#str()
# example:
# Example 1: Converting an integer to a string
text = str(100)
print(text)  # Output: "100"

# Example 2: Converting a float to a string
text = str(3.14)
print(text)  # Output: "3.14"

# Example 3: Converting a boolean to a string
text = str(True)
print(text)  # Output: "True"

# float()
# example:
# Example 1: Converting an integer to a float
number = float(5)
print(number)  # Output: 5.0

# Example 2: Converting a string to a float
number = float("7.89")
print(number)  # Output: 7.89

# Example 3: Converting an integer to a float
number = float(-4)
print(number)  # Output: -4.0


# bool()
# example:
# Example 1: Converting an integer to a boolean
result = bool(0)
print(result)  # Output: False

# Example 2: Converting a non-zero integer to a boolean
result = bool(5)
print(result)  # Output: True

# Example 3: Converting an empty string to a boolean
result = bool("")
print(result)  # Output: False

# 7) მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ, თუ ის არის ნაკიანი დაბეჭდეთ "This is leap year".(ნაკიანი წელიწადი იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე)

# Getting input from the user
year = int(input("Enter a year: "))

# Checking if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a leap year.")
else:
    print("This is not a leap year.")