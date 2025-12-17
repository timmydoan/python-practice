import tuple_convert_list

def get_tuple():
    while True:
        try:
            tup = tuple_convert_list.create_tuple()
            tup = tuple(int(x) for x in tup)
            return tup
        except ValueError:
            print("Invalid input. Please try again.")


def find_highest_in_tuple(tup):
    highest_value = max(tup)
    print(f"The highest value in the tuple is: {highest_value}")
    return highest_value

def main():
    tup = get_tuple()
    find_highest_in_tuple(tup)

if __name__ == "__main__":
    main()