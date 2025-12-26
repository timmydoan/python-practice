#Viết hoa chữ cái đầu tiên của chuỗi và viết thường các chữ cái còn lại.
def get_string():
    string = str(input("Enter a string: "))
    return string
  
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

def capitalize_string(string):
    if not string:
        return string
    return string[0].upper() + string[1:].lower()    
def main():
    user_string = get_string()
    capitalized = capitalize_string(user_string)
    word_count = count_words(user_string)
    print(f"Capitalized string: {capitalized}")
    print(f"Number of words: {word_count}")

if __name__ == "__main__":
    main()