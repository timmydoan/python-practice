def get_number():
    num = int(input("Enter an integer number: "))
    return num

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def check_negative_positive(num):
    if num < 0:
        return "Negative"
    elif num > 0:
        return "Positive"
    else:
        return "Zero"
    
def main():
    print("Chechking Numbers: Even/Odd and Negative/Positive")
    number = get_number()
    result_even_odd = check_even_odd(number)
    result_negative_positive = check_negative_positive(number)
    print(f"The number {number} is {result_even_odd} and {result_negative_positive}.")
    
    again = input("Do you want to check another number? (y/n): ")
    if again.lower() == 'y':
        main()
    else:
        print("Thank you for using the Even or Odd Checker. Goodbye!")

if __name__ == "__main__":
    main()

