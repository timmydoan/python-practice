def create_list():
    while True:
        try:
            my_list = []
            total_numbers = int(input("How many numbers do you want to enter? "))
            if total_numbers < 0:
                print("Please enter a number > 0")
                continue
            elif total_numbers == 0:
                print("Can't split an empty list.")
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

def split_list(my_list):
    even_list = [num for num in my_list if num % 2 == 0]
    odd_list = [num for num in my_list if num % 2 != 0]
    return even_list, odd_list

def main():
    print("Creating a list to split into even and odd numbers.")
    my_list = create_list()
    even_list, odd_list = split_list(my_list)
    print("The even numbers are:", even_list)
    print("The odd numbers are:", odd_list)

if __name__ == "__main__":
    main()