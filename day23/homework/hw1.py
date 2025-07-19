#  შეიყვანე სიტყვა, სანამ პირველი და ბოლო ასო არ იქნება თანხმოვანი


def is_consonant(letter):
    vowels = 'აეიოუAEIOUaeiou'
    return letter.isalpha() and letter not in vowels

while True:
    word = input("შეიყვანე სიტყვა: ")
    if len(word) >= 2 and is_consonant(word[0]) and is_consonant(word[-1]):
        break
    else:
        print("პირველი და ბოლო ასო უნდა იყოს თანხმოვანი. სცადე თავიდან.")

print("სწორია! სიტყვა:", word)