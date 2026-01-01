#Change char in string at specific index

def get_string():
    string = str(input("Enter a string: "))
    index = int(input("Enter the index of the character you want to change: "))
    new_char = str(input("Enter the new character: "))
    return string, index, new_char

def change_char(string, index, new_char):
    if index < 0 or index >= len(string):
        return "Index out of range"
    else:
        string = string[:index] + new_char + string[index+1:]
        return string
    
def change_char_at_firts_and_last(string, new_char):
    if len(string) == 0:
        return "String is empty"
    elif len(string) == 1:
        return new_char
    else:
        string = new_char + string[1:-1] + new_char
        return string

def main():
    string, index, new_char = get_string()
    new_string_any_index = change_char(string, index, new_char)
    new_string_first_last = change_char_at_firts_and_last(string, new_char)
    print("The new string with first and last characters changed is: ", new_string_first_last)
    print("The new string is: ", new_string_any_index)

if __name__ == "__main__":
    main()