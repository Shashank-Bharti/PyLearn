Password=input("Enter the password: ")

if (len(Password)<10):
    
    print("Password is too short")
elif (len(Password) >15):
    print("Password is too long")
else :
    print('Password is availiable')