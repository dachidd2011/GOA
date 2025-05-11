# 1)შემოატანინეთ მომხმარებელს რიცხვი  და თუ 10 ზე მეტი იქნება  გამოიტანინოს ("you are right ")
# 2)მომხმარებელს შემოატანინეთ ორი რიცხვი გააკეთეთ მათზე მათემატიკური ოპერაციები  ("+, -, *, /, %, <, >, <=, >=, ==, !=. **) 
# 3)ახსენით დღეს ნასწავლი If კომენტარებით 
# 4)უყურეთ დღევანდელ ჩანაწერს
# 5)sololearn 



# 1. First requirement: Check the number
def check_number():
    number = float(input("Please enter a number: "))
    if number > 10:
        print("you are right")
    else:
        print("The number is less than or equal to 10.")

# 2. Second requirement: Perform mathematical operations on two numbers
def math_operations():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Division by zero is not allowed.")
    print(f"{num1} % {num2} = {num1 % num2}")
    print(f"{num1} < {num2} = {num1 < num2}")
    print(f"{num1} > {num2} = {num1 > num2}")
    print(f"{num1} <= {num2} = {num1 <= num2}")
    print(f"{num1} >= {num2} = {num1 >= num2}")
    print(f"{num1} == {num2} = {num1 == num2}")
    print(f"{num1} != {num2} = {num1 != num2}")
    print(f"{num1} ** {num2} = {num1 ** num2}")





 
 


