# Xóa phần tử trùng lặp khỏi list.

def create_list():
    while True:
        try:
            my_list = []
            total_numbers = int(input("How many numbers do you want?"))
            if total_numbers < 0:
                print("Please enter a number > 0")
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
            continue

# Cách 1: Xóa trùng lặp bằng cách khởi tạo một list mới
# def remove_duplicates(my_list):
#     unique_list = []
#     for item in my_list:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list

#Cách 2: Sử dụng list comprehension (giống cách 1 nhưng ngắn gọn hơn)
def remove_duplicates(my_list):
    unique_list = []
    [unique_list.append(item) for item in my_list if item not in unique_list]
    return unique_list

# Cách 3: Sử dụng set để xóa trùng lặp(nhưng không giữ thứ tự ban đầu)
# def remove_duplicates(my_list):
#     return list(set(my_list))

#Cách 4: Sử dụng dict.fromkeys() (giữ thứ tự ban đầu)
# def remove_duplicates(my_list):
#     return list(dict.fromkeys(my_list))

def main():
    print("Creating a list and removing duplicates.")
    my_list = create_list()
    unique_list = remove_duplicates(my_list)
    print("List after removing duplicates:", unique_list)



main()