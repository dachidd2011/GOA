# 5 სიტყვის შეყვანა, და შენახვა მხოლოდ სწორების



def is_consonant(letter):
    vowels = 'აეიოუAEIOUaeiou'
    return letter.isalpha() and letter not in vowels

correct_words = []

for i in range(5):
    word = input(f"{i+1}) შეიყვანე სიტყვა: ")
    if len(word) >= 2 and is_consonant(word[0]) and is_consonant(word[-1]):
        correct_words.append(word)
    else:
        print("ეს სიტყვა არ აკმაყოფილებს მოთხოვნებს და არ შეინახება.")

print("\nშენახული სიტყვები (სწორი):")
for w in correct_words:
    print("-", w)