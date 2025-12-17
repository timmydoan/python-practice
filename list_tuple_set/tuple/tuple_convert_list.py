#Convert list to tuple
def create_tuple():
    while True:
        try:
            temp_list = []
            total_numbers = int(input("How many values do you want to enter? ")) 
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
                return tuple(temp_list)
        except ValueError: 
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    create_tuple()