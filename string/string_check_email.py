def get_user_email():
    email = str(input("Enter an email address: "))
    return email
    
def check_email(email):
    if email.count("@") != 1:
        return False
    
    local, domain = email.split('@')
   
    if not local or not domain:
        return False
    
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return False
    
    for part in domain_parts:
        if not part.isalpha():
            return False        
    
    return True

def main():
    user_email = get_user_email()
    if check_email(user_email):
        print(f"The email address '{user_email}' is valid.")
    else:
        print(f"The email address '{user_email}' is invalid.")

if __name__ == "__main__":  
    main()