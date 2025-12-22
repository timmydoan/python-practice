def get_string():
    my_string = str(input("Enter a string: "))
    return my_string

def most_frequent(my_string):
    frequency = {}
    for char in my_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    if frequency:
        most_frequent = max(frequency, key=frequency.get)
    else:
        print("The string is empty. Cannot find most frequent character.")
        return None, 0

    tie_count = 0
    for count in frequency.values():
        if count == frequency[most_frequent]:
            tie_count += 1
            if tie_count > 1:
                print("There is a tie for the most frequent character.")
                return None, 0

    return most_frequent, frequency[most_frequent]

def main():
    user_string = get_string()
    most_frequent, count = most_frequent(user_string)
    if most_frequent is not None:
        print(f"The most frequent character is: '{most_frequent}' (appeared {count} times)")

if __name__ == "__main__":
    main()