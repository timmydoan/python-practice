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
                return my_list
        except ValueError:
            print("Invalid input. Please enter an integer value.")
            continue

def get_element_appearance(my_list):
    while True:
        try:
            element = input("Enter the element you want to check for appearance: ")
            count = my_list.count(int(element))
            return element, count
        except ValueError:
            print("Invalid input. Please enter an integer value.")
            continue

def main():
    print("Creating a list and checking element appearance.")
    my_list = create_list()
    element, count = get_element_appearance(my_list)
    if count == 0:
        print(f"The element {element} does not appear in the list.")
    else:
        print(f"The element {element} appears {count} time(s) in the list.")

main()