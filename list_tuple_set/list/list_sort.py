def create_list():
    while True:
        try:
            my_list = []
            total_numbers = int(input("How many numbers do you want to enter? "))
            if total_numbers < 0 :
                print("Please enter a number > 0")
                continue
            elif total_numbers == 0:
                print("Cant sort an empty list.")
                continue
            else:
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
            continue
#Cách 1: Sắp xếp bằng cách sử dụng hàm sort() (thay đổi list ban đầu)
# def sort_list(my_list):
#     increasing_list = sorted(my_list)
#     decreasing_list = sorted(my_list, reverse=True)
#     return increasing_list, decreasing_list

#Cách 2: Bubble Sort
def sort_list(my_list):
    n = len(my_list)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list, my_list[::-1]

    


def main():
    print("Creating a list and sorting it.")
    my_list = create_list()
    increasing_list, decreasing_list = sort_list(my_list)
    print("List sorted in increasing order:", increasing_list)
    print("List sorted in decreasing order:", decreasing_list)

if __name__ == "__main__":
    main()