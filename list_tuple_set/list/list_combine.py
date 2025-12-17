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

def combine_list(my_list):
    print("Create first list:")
    first_list = create_list()

    print("Create second list:")
    second_list = create_list()

    combined_list = first_list + second_list
    return combined_list

def main():
    print("Creating and combining two lists.")
    combined_list = combine_list([])
    print("The combined list is:", combined_list)

if __name__ == "__main__":
    main()
