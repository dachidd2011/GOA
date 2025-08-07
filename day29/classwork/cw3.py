# 3) შექმენით ფუნქცია რომელიც აბრუნებს სიაში უმაღლეს რიცხვს.



def find_highest(numbers):
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest