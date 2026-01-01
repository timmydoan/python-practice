# Function to convert a string to ASCII values and back
def get_string():
    string = str(input("Enter a string: "))
    return string

def string_to_ascii(string):
    ascii_values = [ord(char) for char in string]
    return ascii_values

def ascii_to_string(ascii_values):
    string = ''.join(chr(value) for value in ascii_values)
    return string

def main():
    string = get_string()
    ascii_values = string_to_ascii(string)
    print("The ASCII values are: ", ascii_values)
    decoded_string = ascii_to_string(ascii_values)
    print("The decoded string is: ", decoded_string)

if __name__ == "__main__":
    main()