def get_number():
    while True:
        try:
            original_number = int(input("n ="))
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")  
    return original_number
    
def reverse_number(original_number):
    reversed_number = 0
    while True:
        digit = original_number % 10 
        print("Digit extracted:", digit)
        reversed_number = reversed_number * 10 + digit 
        print("Reversed number so far:", reversed_number)
        original_number = original_number // 10 
        print("Remaining number:", original_number)
        if original_number == 0:
            break
    return reversed_number

def main():
    original_number = get_number()
    reversed_number = reverse_number(original_number)
    print("Reversed number:", reversed_number)

main()
    