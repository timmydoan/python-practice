#Convert list to tuple
def input_list():
    while True:
        try:
            my_list = []
            total_numbers = int(input("how many numbers do you want?"))
            if total_numbers <= 0:
                print("Please enter a positive integer for the number of entries.")
                continue
            for i in range(total_numbers):
                while True:
                    try:
                        num = int(input(f"Enter number {i+1}: "))
                        my_list.append(num)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
            return my_list
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    
def create_tuple_from_list(input_list):
    return tuple(input_list)

def main():
    print("Creating a list of numbers and converting it to a tuple.")
    my_list = input_list()
    my_tuple = create_tuple_from_list(my_list)
    print("The resulting tuple is:", my_tuple)

if __name__ == "__main__":
    main()