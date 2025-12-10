def get_number():
    while True:
        try:
            num = int(input("n ="))
            if 0<= num <= 10: 
                return num
            else:
                print("Please enter an integer between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter an integer value.")

def multiply_numbers(num):
    for i in range(1, 11):
      result = num * i
      print(f"{num} x {i} = {result}")

def main():
    num = get_number()
    multiply_numbers(num)

main()
    