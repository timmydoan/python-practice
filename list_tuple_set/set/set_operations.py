#create set 
def create_set(no_of_elements):
    user_input = input(f"Enter elements of the set {no_of_elements} separated by spaces: ")
    my_set = set(user_input.split())
    return my_set

def operations():
    set1 = create_set(1)
    set2 = create_set(2) 
    print("Set 1:", set1)
    print("Set 2:", set2)
    # Perform set operations
    #Hợp của 2 set: Tất cả phần tử thuộc A hoặc B
    union = set1.union(set2)
    #Giao của 2 set: Thuộc A và B
    intersection = set1.intersection(set2)
    #Hiệu của 2 set: Thuộc A nhưng không thuộc B
    difference = set1.difference(set2)
    #Hiệu đối xứng của 2 set: Thuộc A hoặc B nhưng không thuộc cả hai
    symmetric_difference = set1.symmetric_difference(set2)
    return union, intersection, difference, symmetric_difference

def main():
    union, intersection, difference, symmetric_difference = operations()
    print("Union:", union)
    print("Intersection:", intersection)
    print("Difference (set1 - set2):", difference)
    print("Symmetric Difference:", symmetric_difference)

if __name__ == "__main__":
    main()
    