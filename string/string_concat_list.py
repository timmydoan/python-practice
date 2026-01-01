#Combine list of strings into a single string
def get_string_list():
    str_list = []
    n = int(input("Enter the number of strings to concatenate: "))
    for i in range(n):
        string = str(input(f"Enter string {i + 1}: "))
        str_list.append(string)
    return str_list

def concatenate_strings(str_list):
    result = " ".join(str_list)
    return result

def main():
    string_list = get_string_list()
    concatenated_string = concatenate_strings(string_list)
    print(f"Concatenated string: {concatenated_string}")
    print(type(concatenated_string))

if __name__ == "__main__":
    main()