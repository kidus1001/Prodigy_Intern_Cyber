min_len = 8

def inputPassword ():
    print ("Enter password: ", end="")
    pw = input()
    return pw

flag = True
goodPW = False

while flag:
    pw = inputPassword()
    
    upperCheck = False
    lowerCheck = False
    numberCheck = False
    specialCharCheck = False
    
    for i in range(len(pw)):
        if pw[i].lower() == pw[i]:
            lowerCheck = True
        if pw[i].upper() == pw[i]:
            upperCheck = True
        if pw[i].isdigit():
            numberCheck = True
        if not pw[i].isalnum() and not pw[i].isspace():
            specialCharCheck = True
            
    if pw == "":
        print ("Password can't be empty! Try again!")
        goodPW = False
    elif len(pw) < min_len:
        print (f"Length of password must be atleast {min_len}")
        goodPW = False
    else:
        if not upperCheck:
            print("Password must contain atleast 1 uppercase letter!")
        if not lowerCheck:
            print("Password must contain atleast 1 uppercase letter!")
        if not specialCharCheck:
            print("Password must contain atleast 1 special character!")
        if not numberCheck:
            print("Password must contain atleast 1 number!")
            
        if upperCheck and lowerCheck and specialCharCheck and numberCheck:
            goodPW = True
    
    if goodPW:
        print ("Valid password! Done!")
        flag = False