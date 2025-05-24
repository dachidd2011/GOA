#1)მომხმარებელს შემოატანინეთ სამი რიცხვი, start/end/step და ჩასვით for loop-ში სათანადო ადგილას.
#2)მომხმარებელს შემოატანინეთ რიცხვი და დაპრინტეთ რიცხვი ყოველ იტერაციაზე იქამდე, სანამ რიცხვი მომხმარებლის რიცხვს არ გაუტოლდება (While Loop)












# 1)
start = int(input("შეიყვანეთ საწყისი რიცხვი (start): "))
end = int(input("შეიყვანეთ საბოლოო რიცხვი (end): "))
step = int(input("შეიყვანეთ ნაბიჯი (step): "))
for i in range(start, end, step):
    print(i)

# 2)
target = int(input("შეიყვანეთ რიცხვი: "))

i = 0

while i <= target:
    print(i)
    i += 1

#3)
target = int(input("შეიყვანეთ რიცხვი: "))

for i in range(0, target + 1):
    print(i)
