def get_name():
    name = str(input("Enter a full name: "))
    return name

def split_name(full_name):
    name_parts = full_name.split()
    if len(name_parts) < 2:
        print("Please enter at least a first name and a last name.")
        return None, None
    elif len(name_parts) > 2:
        first_name = name_parts[0]
        last_name = " ".join(name_parts[-2:])
    else:
        first_name = name_parts[0]
        last_name = name_parts[1]
    return first_name, last_name

def main():
    full_name = get_name()
    first_name, last_name = split_name(full_name)
    if first_name and last_name:
        print(f"First name, {first_name}")
        print(f"Last name, {last_name}")

if __name__ == "__main__":
    main()