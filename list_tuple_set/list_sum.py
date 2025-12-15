#Tổng tất cả các phần từ trong list 
def create_list():
    
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
    
def sum_list(my_list):
    total = 0
    for num in my_list:
        total += num
    return total

def main():
    print("Creating a list of numbers and calculating their sum.")
    my_list = create_list()
    total_sum = sum_list(my_list)
    print("The sum of the numbers in the list is:", total_sum)

if __name__ == "__main__":
    main()