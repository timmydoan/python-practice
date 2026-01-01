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
    
def main():
    string, index, new_char = get_string()
    new_string = change_char(string, index, new_char)
    print("The new string is: ", new_string)

if __name__ == "__main__":
    main()