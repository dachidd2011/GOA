#  1) შექმენით უსასრულო while loop
# 2) გამოიტანეთ მომხმარებლის შემოყვანილი სახელი 10-ჯერ იტერაციის მეშვეობით
# 3) შექმენით while loop და კომენტარად მიაწერეთ რომელია თავი და რომელი სხეული












#  1) შექმენით უსასრულო while loop
while True:
    print("hello")


# 2) გამოიტანეთ მომხმარებლის შემოყვანილი სახელი 10-ჯერ იტერაციის მეშვეობით
while i<10:
    print("hello")
    i = i +1


# 3) შექმენით while loop და კომენტარად მიაწერეთ რომელია თავი და რომელი სხეული

ount = 0

while count < 5:  # This is the loop head (condition)
    print("Hello!")  # This is the loop body
    count += 1  # makes the counter to eventually end the loop


# 4) მომხმარებელს შემოაყვანინეთ რიცხვი, სანამ ეს რიცხვი არ იქნება 100-ზე მეტი მაქამდე თავიდან მოთხოვთ რიცხვის შემოტანა

number = int(input("Enter a number greater than 100: "))

while number <= 100:  
    number = int(input("Invalid! Please enter a number greater than 100: "))

print("Thank you! You entered:", number)

# 5) მომხმარებელს შემოატანინეთ სხვადასხვა სახელები 5-ჯერ იტერაციის მეშვეობით, შექმენით ამ სახელებისთვის ცვლადი რომელშიც ყოველი სახელი დაემატება და ეს სახელები გამოიყოფა მძიმეებით, ანუ თქვენი ცვლადი 5 სახელის შეყვანის შემდეგ უნდა გამოიყურებოდეს ასე: "{სახელი პირველი}, {სახელი მეორე}, ... {სახელი მეხუთე}"

for i in range(5):
    name = input(f"Enter name #{i + 1}: ")

    if i < 4:
        names += name + ", "
    else:
        names += name  # No comma after the last name

print("The names are:", names)