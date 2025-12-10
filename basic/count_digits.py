def get_number():
    while True:
        try:
            num = float(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def count_digits(num):
    num_str = str(num).replace('.', '').replace('-', '')
    return len(num_str)

def main():
    num = get_number()
    digits_count = count_digits(num)
    print(f"The number {num} has {digits_count} digits (excluding decimal point and sign).")

main()