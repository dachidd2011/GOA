# 3) შექმენით ფუნქცია, რომელიც იღებს წინადადებას, სადაც ყოველი სიტყვის შორის ერთზე მეტი დაშორებაა(space).
#  თქვენი დავალებაა ჩამოაშოროთ გადმოცემულ წინადადებას ზედმეტი space-ები(სიტყვებს შორის მხოლოდ ერთი უნდა იყოს).
#  საბოლოოდ დააბრუნეთ ეს წინადადება




def remove_extra_spaces(sentence):
    new_sentence = ''
    space_found = False
    
    for char in sentence:
        if char != ' ':
            new_sentence += char
            space_found = False
        else:
            if not space_found:
                new_sentence += ' '
                space_found = True
           

    return new_sentence.strip()  