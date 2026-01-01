import random 

def generate_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def main():
    length = int(input("Enter the length of the random string: "))
    random_string = generate_random_string(length)
    print("The generated random string is: ", random_string)

if __name__ == "__main__":
    main()