def create_string():
    my_string = str(input("Enter a string: "))
    return my_string

def get_user_check(string):
    sub = str(input("Enter the substring to check: "))
    return sub

def check_substring(string, sub):
    if sub in string:
        print(f"The substring '{sub}' IS present in the string.")
    else:
        print(f"The substring '{sub}' IS NOT present in the string.")

def main():
    user_string = create_string()
    substring = get_user_check(user_string) 
    check_substring(user_string, substring)

if __name__ == "__main__":
    main()