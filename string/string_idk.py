def get_string():
    string = str(input("Enter a string: "))
    return string
  
def capitalize_string(string):
    if not string:
        return string
    return string[0].upper() + string[1:].lower()

def count_words(string):
    words = 0 
    in_word = False
    for letter in string:
        if letter == " ":
            in_word = False
        elif not in_word:
            words += 1
            in_word = True
    return words