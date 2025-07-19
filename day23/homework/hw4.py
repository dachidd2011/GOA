# 10 სიტყვის შეყვანა და მხოლოდ სწორის დაბეჭდვა


def is_consonant(letter):
    vowels = 'აეიოუAEIOUaeiou'
    return letter.isalpha() and letter not in vowels

correct_words = []

for i in range(10):
    word = input(f"{i+1}) შეიყვანე სიტყვა: ")
    if len(word) >= 2 and is_consonant(word[0]) and is_consonant(word[-1]):
        correct_words.append(word)

print("\n✅ სწორი სიტყვები:")
if correct_words:
    for w in correct_words:
        print("-", w)
else:
    print("სწორი სიტყვა არ იქნა შეყვანილი.")
