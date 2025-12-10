def get_number():
    while True:
        try:
            num = int(input("Nummber to check: "))
            if num <= 0:
                print("Negative numbers is not prime number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a natural numbers.")
            continue
        break
    return num

def check_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
def main():
    num = get_number()
    if check_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

if __name__ == "__main__":
    main()