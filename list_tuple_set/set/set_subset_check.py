from set_operations import create_set

def is_subset(set1, set2):
    return set1.issubset(set2)

def main():
    set1 = create_set(1)
    set2 = create_set(2)
    print("Set 1:", set1)
    print("Set 2:", set2)
    
    if is_subset(set1, set2):
        print("Set 1 is a subset of Set 2")
    else:
        print("Set 1 is not a subset of Set 2")

if __name__ == "__main__":
    main()
