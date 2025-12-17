def get_a():
    while True: 
        try:
            a = float(input("a ="))
            if a == 0:
                print("Value of 'a' cannot be 0 for a linear equation.")
                continue
            return a
        except ValueError:
            print("Invalid input. Please enter a non-zero numeric value for 'a'.")
            continue

def get_b():
    while True:
        try:
            b = float(input("b =")) 
            return b
        except ValueError:
            print("Invalid input. Please enter a numeric value for 'b'.")
            continue
    

def find_x(a, b):
    x = -b / a 
    return x

def main():
    print("For equation ax + b = 0, enter a and b:")
    a = get_a()
    b = get_b()
    x = find_x(a, b)
    print(f"x = {x}")

if __name__ == "__main__":
    main()