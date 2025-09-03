# 6) dictionary ფასებით:

# products = {
#     "apple": 3,
#     "banana": 2,
#     "milk": 5
# }


# დაბეჭდე ყველა პროდუქტი for loop-ით.

# მომხმარებლისგან შეიყვანე პროდუქტი, თუ არსებობს → დაბეჭდე ფასი.

# დაამატე ახალი პროდუქტი update()-ით.

# ბოლოს გამოიყენე clear() ჩასაშენებლად, მაგალითად, ცარიელი dictionary-ს დაბეჭდვა დასუფთავების შემდეგ.





products = {
    "apple": 3,
    "banana": 2,
    "milk": 5
}

print("ყველა პროდუქტი:")
for product, price in products.items():
    print(product, "→", price)

user_input = input("\nმიუთითე პროდუქტი: ")

if user_input in products:
    print(f"{user_input}-ის ფასი არის {products[user_input]}")
else:
    print("ასეთი პროდუქტი არ არსებობს!")

products.update({"bread": 4})
print("\nახალი პროდუქტების სია:", products)

products.clear()
print("\nდასუფთავების შემდეგ:", product)