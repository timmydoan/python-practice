def get_a():
    a = float(input("Enter first number: "))
    return a

def get_b():
    b = float(input("Enter second number: "))
    return b

def get_c():
    c = float(input("Enter third number: "))
    return c

def find_highest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    
    
def main():     
    print("Do you want to see the highest value among the three numbers? (y/n): ")
    choice = input().lower()
    if choice == 'y':
        a = get_a()
        b = get_b()
        c = get_c()
        highest_value =find_highest(a, b, c)
        print(f"The highest value is: {highest_value}")
    else:
        print("Thank you for using the highest number finder. Goodbye!")
    

main()

