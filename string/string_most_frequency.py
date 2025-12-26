def get_string():
    my_string = str(input("Enter a string: "))
    return my_string

def most_frequent(my_string):
    frequency = {}
    #Đếm xem cái nào xuất hiện nhiều nhất
    for char in my_string:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1

    #Nếu có nhiều nhất thì lấy kết quả cái nhiều nhất, không có thì trả ra None
    if frequency:
        most_frequent_char = max(frequency, key=frequency.get)
    else:
        print("The string is empty. Cannot find most frequent character.")
        return None, 0

    #Xử lý trường những chữ xuất hiện nhiều nhất thì lại xuất hiện bằng nhau
    tie_count = 0 #Đếm số lần xuất hiện của các ký tự có tần số bằng nhau
    for count in frequency.values():
        if count == frequency[most_frequent_char]: #so sảnh biến count với value của ký tự xuất hiện nhiều nhất
            tie_count +=1
            if tie_count > 1:
                print("There is a tie for the most frequent character.")
                return None, 0

    return most_frequent_char, frequency[most_frequent_char]

def main():
    user_string = get_string()
    most_frequent, count = most_frequent(user_string)
    if most_frequent is not None:
        print(f"The most frequent character is: '{most_frequent}' (appeared {count} times)")

if __name__ == "__main__":
    main()