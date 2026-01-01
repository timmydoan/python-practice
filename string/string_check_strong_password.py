#Check if the password is strong or not 
def get_password():
    password = str(input("Enter a password you want to check: "))
    return password

def checking_password(password):
    if len(password) < 8:
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char.lower() for char in password):
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char in "!@#$%^&*()-+" for char in password):
        return False
    else:
        return True
    
def main():
    password = get_password()
    checking_password(password)
    if checking_password(password) == True:
        print ("Password is strong. ")
    else:
        print ("Password is weak. ")

if __name__ == "__main__":
    main()
    
    