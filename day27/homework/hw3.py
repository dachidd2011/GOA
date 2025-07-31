# 3) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას while
#  ციკლით და ჩაამატეთ გაორმაგებული რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია




def double_numbers(numbers):
    i = 0
    doubled = []
    while i < len(numbers):
        doubled.append(numbers[i] * 2)
        i += 1
    return doubled