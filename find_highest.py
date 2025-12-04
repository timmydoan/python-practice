def create_list_and_find():
    numbers = []
    while True:
        try: 
            total_numbers = float(input("How many numbers do you want to enter? "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    for i in range(int(total_numbers)):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    
    return print(f"The list of numbers you entered is: {numbers}"),  print(f"The highest number in the list is: {max(numbers)}")             

create_list_and_find()