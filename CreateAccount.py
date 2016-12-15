#Cesar Neri
#December 15, 2016

#Excercise 10-1 from Murach's Python Programming Book



#!/usr/bin/env python3

def main():
    full_name = get_full_name()
    print()
    password = get_password()
    print()
    email = get_email()
    print()
    phone = get_phone()
    print()
    first_name = get_first_name(full_name)   
    print("Hi " + first_name + ", thanks for creating an account.")
    print("We will text your confirmation to this number: " + phone)
    
def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
    
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name
    
def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print("Password must be 8 characters or more \n" +
                  "with at least one digit and one uppercase letter.")
        else:
            return password

def get_email():
    while True:
        email = input("Enter email:       ").strip()

        #check that email contains @  AND #check that it ends with '.com'
        if "@" in email and email[-4:] == ".com":
                break
        else:
            print("Email must contain one '@' character and end with '.com'")

    return email

def get_phone():
    while True:
        phone = input("Enter phone number:       ").strip()

        #remove all extra characters
        phone = phone.replace(" ", "")
        phone = phone.replace("(", "")
        phone = phone.replace(")", "")
        phone = phone.replace("-", "")

        #check that is all digits and is 10 characters long
        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("Phone must contain 10 digits.")

        
    phone = phone[0:3] + "." + phone[3:6] + "." + phone[6:]
    return phone
        
if __name__ == "__main__":
    main()
