#remove sprecial characters from string
def get_string():
    my_string = str(input("Enter a string: "))
    return my_string

def remove_special_characters(my_string):
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~\\"
    cleaned_string = ""
    for char in my_string:
        if char not in special_characters:
            cleaned_string += char
    return cleaned_string

def main():
    user_string = get_string()
    cleaned_string = remove_special_characters(user_string)
    print(f"String after removing special characters: {cleaned_string}")

if __name__ == "__main__":
    main()