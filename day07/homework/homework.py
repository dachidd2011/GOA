# 1)დაწერე პროგრამა, რომელიც while ციკლით დაბეჭდავს რიცხვებს 1-დან 10-მდე.
# 2)დაწერე პროგრამა, რომელიც დაბეჭდავს რიცხვებს 10-დან 1-მდე.
# 3)კომენტარებით ახსენი while loop. 
# 4)დაწერე პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. სწორი პაროლია "python123". სანამ სწორად არ შეიყვანს, მოთხოვე თავიდან.
# 5)მომხმარებელმა უნდა შეიყვანოს რიცხვი n. პროგრამამ while ციკლით უნდა დაითვალოს 1-დან n-მდე რიცხვების ჯამი.




# 1)დაწერე პროგრამა, რომელიც while ციკლით დაბეჭდავს რიცხვებს 1-დან 10-მდე.

i = 1
while i <= 10:
    print(i)
    i += 1


# 2)დაწერე პროგრამა, რომელიც დაბეჭდავს რიცხვებს 10-დან 1-მდე.

i = 10
while i >= 1:
    print(i)
    i -= 1


# 3)კომენტარებით ახსენი while loop:
# while loop is used to repeat a block of code as long as a condition is True
#If the condition is false at the beginning, the loop won’t run at all


# 4)დაწერე პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. სწორი პაროლია "python123". სანამ სწორად არ შეიყვანს, მოთხოვე თავიდან.

correct_password = "python123"

password = input("Enter the password: ")

while password != correct_password:
    print("Incorrect password. Please try again.")
    password = input("Enter the password: ")

print("Access granted.")


# 5)მომხმარებელმა უნდა შეიყვანოს რიცხვი n. პროგრამამ while ციკლით უნდა დაითვალოს 1-დან n-მდე რიცხვების ჯამი.


n = int(input("Enter a number: "))


i = 1
total = 0


while i <= n:
    total += i  
    i += 1      


print("The sum from 1 to", n, "is:", total)