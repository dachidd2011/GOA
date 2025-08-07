# 5) შექმენით ფუნქცია, რომელსაც გადაეცემა წინადადება. თქვენი დავალებაა ამ წინადადების სიტყვები შეაბრუნოთ და დააბრუნოთ(სიტყვების 
# სიმბოლოები არ უნდა იყოს შებრუნებული) 





def reverse_word_order(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)