# 1) შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას, ფუნქციამ ამ წინადადების თითოეული სიტყვა უნდა შეინახოს სიაში, 
# როგორც ცალკე ელემენტი. საბოლოოდ გადააქციეთ სია ისევ წინადადებად, სადაც სიტყვებს შორის არის მძიმე და ერთი დაშორება(", ")


def transform_sentence(text):
    lst = []
    word = ''
    
    for char in text:
        if char != ' ':
            word += char
        else:
            lst.append(word)
            word = ''
    lst.append(word) 
    
    return ', '.join(lst)