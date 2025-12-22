#Tìm phần từ xuất hiện nhiều nhất trong list

def create_list():
    while True:
        try: 
            my_list = []
            total_numbers = int(input("How many numbers do you want?"))
            if total_numbers < 0: 
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

def find_most_frequent_element(my_list):
    frequency = {}
    for item in my_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    
    if frequency:
        most_frequent = max(frequency, key=frequency.get)
    else:
        print("The list is empty. Cannot find most frequent element.")
        return None, 0
    
    tie_count = 0
    for count in frequency.values(): 
        if count == frequency[most_frequent]:
            tie_count += 1
            if tie_count > 1:
                print("There is a tie for the most frequent element.")
                return None, 0

    return most_frequent, frequency[most_frequent]

def main():
    print("Creating a list and finding the most frequent element.")
    my_list = create_list()
    most_frequent, count = find_most_frequent_element(my_list)
    if most_frequent is not None:
        print(f"The most frequent element is: {most_frequent} (appeared {count} times)")

if __name__ == "__main__":
    main()