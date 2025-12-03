import math
def area_of_rectangle(length, width):
    rectangle_area = length * width
    return rectangle_area

def area_of_circle(radius):  
    circle_area = math.pi * radius ** 2
    return circle_area

def area_of_square(side):
    square_area = side ** 2
    return square_area

def area_of_triangle(base, height):
    triangle_area = 0.5 * base * height
    return triangle_area

options = {
    1: area_of_rectangle,
    2: area_of_circle,
    3: area_of_square,
    4: area_of_triangle
}
def get_choice():
    print("Select the shape to calculate area:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Square")
    print("4. Triangle")

    user_choice = int(input("Enter your choice (1-4): "))
    return user_choice

def get_dimensions(user_choice):
    print("Enter the dimensions of the shape.")
    if user_choice == 1:
        length = float(input("Enter the length of the rectangle: "))       
        width = float(input("Enter the width of the rectangle: "))
        return length, width
    elif user_choice == 2:
         radius = float(input("Enter the radius of the circle: "))
         return radius
    elif user_choice == 3:
         side = float(input("Enter the side of the square: "))
         return side
    elif user_choice == 4:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        return base, height
    else:
        print("Invalid choice. Please select a number between 1 and 4.")
        return None
def main():
    user_choice = get_choice()
    dimensions = get_dimensions(user_choice)

    if user_choice == 1:
        area = options[user_choice](*dimensions)
        print(f"The area of the rectangle is: {area}")
    elif user_choice == 2:
        area = options[user_choice](dimensions)
        print(f"The area of the circle is: {area}")
    elif user_choice == 3:
        area = options[user_choice](dimensions)
        print(f"The area of the square is: {area}")
    elif user_choice == 4:
        area = options[user_choice](*dimensions)
        print(f"The area of the triangle is: {area}")
    else:
        print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()