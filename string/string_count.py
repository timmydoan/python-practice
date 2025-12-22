def get_string():
    string = str(input("Enter a string: "))
    return string

def count_characters(string):
    count = len(string)
    return count

def main():
    user_string = get_string()
    character_count = count_characters(user_string)
    print(f"The string '{user_string}' has {character_count} characters.")

if __name__ == "__main__":
    main()