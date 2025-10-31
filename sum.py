def get_a():
    a = int(input("Enter first number: "))
    return a
def get_b():
    b = int(input("Enter second number: "))
    return b

def plus(a, b):
    c = a + b
    return print(f"The sum is: {c}")

def main():
    a = get_a()
    b = get_b()
    plus(a, b)

main()