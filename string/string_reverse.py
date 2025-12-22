my_string = "hello world"
def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s

    return reversed_s

def main():
    print("Original string:", my_string)
    reversed_str = reverse_string(my_string)
    print("Reversed string:", reversed_str)

if __name__ == "__main__":
    main()