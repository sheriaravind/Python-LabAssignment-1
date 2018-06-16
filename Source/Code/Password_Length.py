import re

Numbers = r'[0-9]'
Special_Characters = r'[!@*$]'
Upper_Case = r'[A-Z]'
Lower_Case = r'[a-z]'

def get_Password():
    password = input("Enter the Password!")
    Password_Characteristics(password)

def Password_Characteristics(password):

    if(len(password) < 6):
        print("Password is too short and should have atleast 6 characters")
        get_Password()

    elif(len(password) > 16):
        print("Password is too big and should be of maximum ength 16 characters")
        get_Password()

    elif(re.search(Numbers,password) == None):
        print("Password should have atleast one number")
        get_Password()

    elif(re.search(Special_Characters,password) == None):
        print("Password should have atleast one special character !,@,$,*")
        get_Password()

    elif(re.search(Upper_Case,password) == None):
        print("Password should have atleast one Upper Case Letter")
        get_Password()

    elif(re.search(Lower_Case, password) == None):
        print("Password should have atleast have one lower case letter")
        get_Password()

    else:
        print("Entered Password matches all the cases")

if __name__ == '__main__':
    get_Password()