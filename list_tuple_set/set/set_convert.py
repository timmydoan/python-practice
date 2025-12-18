def create_list():
    while True:
            try:
                temp_list = []
                total_numbers = int(input("How many values do you want to enter in a List? ")) 
                if total_numbers < 0 :
                    print("Please enter a number > 0")
                    continue
                elif total_numbers == 0:
                    print("Cant work with an empty tuple.")
                    continue
                else:
                    for i in range(total_numbers):
                        while True:
                            value = input(f"Enter value no.{i+1}:")
                            try:
                                if '.' in value:
                                    value = float(value)
                                else:
                                    value = int(value)
                            except ValueError:
                                pass
                            temp_list.append(value)
                            break
                    return temp_list
            except ValueError: 
                print("Invalid input. Please enter a numeric value.")
def create_set():
    user_input = input(f"Enter elements of the set separated by spaces: ")
    temp_set = set(user_input.split())
    return temp_set
    

def convert(temp_list, temp_set):
    result_list = list(temp_set)
    result_set = set(temp_list)
    return result_list, result_set

def main():
    temp_list = create_list()
    temp_set = create_set()
    print("The created list is:", temp_list)
    print("The created set is:", temp_set)
    result_list, result_set = convert(temp_list, temp_set)
    
    print("The created list from set is:", result_list)
    
    print("The created set from list is:", result_set)

if __name__ == "__main__":
    main()