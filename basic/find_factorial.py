def get_number():
    while True:
        try:
            num = int(input("n ="))
            if num < 0:
                print("Factorial is not defined for negative numbers. Please enter a non-negative integer.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter an integer value.")
            
def find_factorial(num):
    if num == 0 or num == 1:
        return 1 
    else: 
        result = 1
        for i in range (1, num ):
            result = result * (i + 1)
        return result

def main():
    num = get_number()
    result = find_factorial(num)
    print (result)

main()
    
       