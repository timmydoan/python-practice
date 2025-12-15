def create_list():
    while True:
        try:
            my_list = []
            total_numbers = int(input("How many numbers do you want to enter? "))
            if total_numbers < 0:
                print("Please enter a number > 0")
                continue
            elif total_numbers == 0:
                print("Can't combine an empty list.")
                continue
            else:
                for i in range(total_numbers):
                    while True:
                        try:
                            num = int(input(f"Enter number {i+1}:"))
                            my_list.append(num)
                            break
                        except ValueError:
                            print("Invalid input. Please enter an integer value.")
                            continue
                return my_list
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

def filter_even_numbers(my_list):
    even_numbers = [num for num in my_list if num % 2 == 0]
    return even_numbers

def main():
    print("Creating a list and filtering even numbers.")
    my_list = create_list()
    even_numbers = filter_even_numbers(my_list)
    print("The new list with only even numbers is:", even_numbers)

main()