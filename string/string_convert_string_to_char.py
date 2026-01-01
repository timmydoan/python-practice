#Convert string to char array and back
def get_string():
    my_string = str(input("Enter a string: "))
    return my_string

def string_to_char_array(my_string):
    char_array = [char for char in my_string]
    return char_array

def char_array_to_string(char_array):
    my_string_from_array = ''.join(char_array)
    return my_string_from_array

def main():
    my_string = get_string()
    char_array = string_to_char_array(my_string)
    print("The character array is: ", char_array)
    my_string_from_array = char_array_to_string(char_array)
    print("The string is: ", my_string_from_array)

if __name__ == "__main__":
    main()