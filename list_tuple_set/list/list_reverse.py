def create_list():
    while True:
        try:
            my_list = []
            total_numbers = int(input("How many numbers do you want to enter?"))
            if total_numbers < 0:
                print("Please enter a number > 0")
                continue
            elif total_numbers == 0:
                print("Can't reverse an empty list.")
                continue
            else:
                for i in range(total_numbers):
                    while True:
                        value = input(f"Enter a value {i+1}:")
                        try: 
                            if '.' in value:
                               value = float(value)
                            else:
                               value = int(value)
                        except ValueError:
                            pass
                        my_list.append(value)
                        break
                return my_list
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

def reverse_list(my_list):
    reversed_list = my_list[::-1]
    return reversed_list

def main():
    print("Creating a list and reversing it.")
    my_list = create_list()
    print("The original list is:", my_list)
    reversed_list = reverse_list(my_list)
    print("The reversed list is:", reversed_list)

if __name__ == "__main__":
    main()