# სიტყვის ანალიზი — დაითვალე ხმოვნები და თანხმოვნები, სანამ სწორი არ იქნება


def is_consonant(letter):
    vowels = 'აეიოუAEIOUaeiou'
    return letter.isalpha() and letter not in vowels

def is_vowel(letter):
    vowels = 'აეიოუAEIOUaeiou'
    return letter.lower() in vowels

while True:
    word = input("შეიყვანე სიტყვა: ")
    vowels_count = 0
    consonants_count = 0

    for char in word:
        if char.isalpha():
            if is_vowel(char):
                vowels_count += 1
            else:
                consonants_count += 1

    print(f" ხმოვნები: {vowels_count}, თანხმოვნები: {consonants_count}")

    if len(word) >= 2 and is_consonant(word[0]) and is_consonant(word[-1]):
        print(" სწორი სიტყვა! პროგრამა დასრულდა.")
        break
    else:
        print(" სიტყვა არ არის სწორი. სცადე თავიდან.\n")