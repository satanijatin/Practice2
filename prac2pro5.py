password = input("Enter a password: ")


if 6 <= len(password) <= 16:
 
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special_char = False


    for char in password:
       
        if char.islower():
            has_lowercase = True
      
        elif char.isupper():
            has_uppercase = True
       
        elif char.isdigit():
            has_digit = True
       
        elif char in ['$','#','@']:
            has_special_char = True

   
    if has_lowercase and has_uppercase and has_digit and has_special_char:
        print("Password is valid.")
    else:
        print("Password is invalid. Please check the requirements.")
else:
    print("Password length should be between 6 and 16 characters.")
