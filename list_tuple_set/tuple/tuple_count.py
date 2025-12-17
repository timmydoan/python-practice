def create_tuple():
    while True:
        try:
            temp_list = []
            total_numbers = int(input("How many numbers do you want to enter? ")) 
            if total_numbers < 0 :
                print("Please enter a number > 0")
                continue
            elif total_numbers == 0:
                print("Cant count an empty tuple.")
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
                return tuple(temp_list)
        except ValueError: 
            print("Invalid input. Please enter a numeric value.")


tup = create_tuple()

def count_element_in_tuple(my_tuple):
    search_value = input("Enter the element you want to count: ")
    try:
        if '.' in search_value:
            target = float(search_value)
        else:
            target = int(search_value)
    except ValueError:
        target = search_value
    count = my_tuple.count(target)
    return target, count

def main():
    if len(tup) == 0:
        print("The tuple is empty.")
        return
    target, count = count_element_in_tuple(tup)
    print(f"The element {target} appears {count} time(s) in the tuple.")

if __name__ == "__main__":
    main()