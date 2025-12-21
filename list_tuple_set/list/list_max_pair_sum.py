my_list = [1, 2, 3, 4, 5]

def max_pair_sum(nums):
    max1 = max2 = float('-inf')

    for n in nums:
        if n > max1:
            max2 = max1
            max1 = n         

        elif n > max2:
            max2 = n
    
    return max1, max2, max1 + max2

def main():
    print("The list is:", my_list)
    num1, num2, total = max_pair_sum(my_list)
    print(f"The two highest numbers are: {num1} and {num2}")
    print(f"Their sum is: {total}")

if __name__ == "__main__":      
    main()