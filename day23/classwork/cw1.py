# 1) მომხმარებელს შემოატანეთ ინფუთი სანამ პირველი და ბოლო ასო ინფუთის არ იქნება ხმოვანი


def is_consonant(char):
    return char.lower() not in 'აეიოუ' and char.isalpha()

while True:
    text = input("შეიყვანეთ სტრინგი: ")

    if len(text) >= 1 and is_consonant(text[0]) and is_consonant(text[-1]):
        print("სტრინგის პირველი და ბოლო ასო თანხმოვანია!")
        break
    else:
        print("სტრინგის პირველი ან ბოლო ასო არ არის თანხმოვანი. სცადეთ თავიდან.")