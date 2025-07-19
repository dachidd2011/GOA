# დაითვალე, რამდენჯერ სცადა სწორი სიტყვის შეყვანა


def is_consonant(letter):
    vowels = 'აეიოუAEIOUaeiou'
    return letter.isalpha() and letter not in vowels

correct_words = []
attempts = 0  

while len(correct_words) < 5:
    word = input(f"{len(correct_words)+1}) შეიყვანე სიტყვა: ")
    attempts += 1
    if len(word) >= 2 and is_consonant(word[0]) and is_consonant(word[-1]):
        correct_words.append(word)
    else:
        print(" ეს სიტყვა არ აკმაყოფილებს მოთხოვნებს და არ შეინახება.")

print("\n შენახული სწორი სიტყვები:")
for w in correct_words:
    print("-", w)

print(f"\n ჯამში შენ სცადე {attempts} ჯერ სწორი სიტყვების შეყვანა.")