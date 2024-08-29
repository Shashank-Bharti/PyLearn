age = int(input("Enter your age: "))

#if statement no.1
if (age >= 18):
    print(age, "You're an adult")
    print('Damn!')
#end of If_1
    
#if statement no.2
if (age >= 100):
    print("You're a century old")

    
elif age <= 0:
    print("Please enter a valid age")
    
else:
    print(age, "You're a minor")

#end of If_2    
    