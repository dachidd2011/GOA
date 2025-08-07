# 2) შექმენით ფუნქცია რომელიც მიიღებს რიცხვების სიას და დაბრუნებს მხოლოდ ლუწების ჯამს.


def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

