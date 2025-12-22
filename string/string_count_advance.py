def get_string():
    my_string = str(input("Enter a string: "))
    return my_string


def count_upper_lower(string):
    count_upper_letters = 0
    count_lower_letters = 0

    for char in string:
        if char.isupper():
            count_upper_letters += 1
        elif char.islower():
            count_lower_letters += 1

    return count_upper_letters, count_lower_letters

def count_vowels_consonants(string):
    vovels = 0
    consonants = 0

    for char in string:
        if char in "aeiouAEIOU":
            vovels += 1
        elif char.isalpha():
            consonants += 1

    return vovels, consonants    

def main():
    user_string = get_string()
    upper_count, lower_count = count_upper_lower(user_string)
    vowel, consonant = count_vowels_consonants(user_string)

    print(f"The string '{user_string}' has {upper_count} uppercase letters and {lower_count} lowercase letters.")
    print(f"The string '{user_string}' has {vowel} vowels and {consonant} consonants.")

if __name__ == "__main__":
    main()