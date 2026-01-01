def get_string():
    string = str(input("Enter a string: "))
    return string

def get_word_want_to_count():
    word = str(input("Enter the word you want to count: "))
    return word

def count_duplicate(string, word):
    words = string.split()
    count = words.count(word)
    return count    

def main():
    string = get_string()
    word = get_word_want_to_count()
    count = count_duplicate(string, word)
    print(f"The word '{word}' appears {count} times in the given string.")

if __name__ == "__main__":
    main()