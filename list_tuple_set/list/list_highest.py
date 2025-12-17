#Nhập danh sách số và in số lớn nhất trong danh sách

def create_list():
    while True:
        try:
            my_list = []
            total_numbers = int(input("How many numbers do you want to enter? "))
            if total_numbers < 0:
                print("Please enter a positive integer for the number of entries.")
                continue
            elif total_numbers == 0:
                print("Can't find the highest number in an empty list.")
                continue
            else:
                for i in range(total_numbers):
                    while True:
                        try:
                            numm = float(input(f"Enter number {i+1}: "))
                            my_list.append(numm)
                            break
                        except ValueError:
                            print("Invalid input. Please enter a numeric value.")
                return my_list
        except (ValueError, IndexError):
            print("Invalid input. Please enter numeric values.")

def find_highest_number(my_list):
    highest = my_list[0]
    for num in my_list:
        if num > highest:
            highest = num
    return highest

def main():
    my_list = create_list()
    highest_number = find_highest_number(my_list)
    print("The highest number in the list is:", highest_number)

if __name__ == "__main__":
    main()