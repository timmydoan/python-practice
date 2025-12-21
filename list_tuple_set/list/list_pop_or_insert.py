#Xoá phần tử hoặc thêm phần tử theo chỉ số 
def create_list():
    while True:
        try:
            my_list = []
            total_numbers = int(input("How many value do you want to enter? "))
            if total_numbers < 0:
                print("Please enter a number > 0")
                continue 
            elif total_numbers == 0:
                print("Can't work with an empty list.")
                continue
            else:
                for i in range(total_numbers):
                    value_in_list = input(f"Enter value {i + 1}: ")
                    my_list.append(parse_value(value_in_list))
                return my_list
        except ValueError:
            print("Invalid input. Please enter an integer value.")
            continue 

def get_index(my_list):
    while True:
        try:
            index = int(input(f"Enter the index (1 - {len(my_list)}): "))
            if index < 1 or index > len(my_list):
                print("Index out of range. Please enter a valid index.")
                continue
            return index - 1  # Convert to 0-based index
        except ValueError:
            print("Invalid input. Please enter an integer value.")
            continue

def delete_by_index(my_list, index):
    return my_list.pop(index)
 

def insert_by_index(my_list, index, new_input_value): 
    my_list.insert(index, new_input_value)

def get_choice():
    while True:
            choice = input("Enter your choice (D/I): ").strip().upper()
            if choice in ['D', 'I']:
                return choice
            print("Invalid choice. Please enter 'D' to delete or 'I' to insert.")
                
def parse_value(input_value):
    try:
        if '.' in input_value:
            return float(input_value)
        return int(input_value)
    except ValueError:
        return input_value

def main():
    my_list = create_list()
    print("The created list is:", my_list)
    
    choice = get_choice()
    
    print("List indices range from 1 to", len(my_list))
    index = get_index(my_list) 
    if choice == 'I':
        new_input_value = parse_value(input("Enter the value to insert: "))
        insert_by_index(my_list, index, new_input_value)
        print("The list after insertion is:", my_list)

    elif choice == 'D':
        removed_element = delete_by_index(my_list, index)
        print(f"The removed element is: {removed_element}")
        print("The list after deletion is:", my_list)

    

if __name__ == "__main__":
    main()

