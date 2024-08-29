#If Elif Else Ladder
age = int(input("Enter your age: "))
if (age >= 18):
    print(age, "You're an adult")
    print('Damn!')
elif age <= 0:
    print("Please enter a valid age")
else:
    print(age, "You're a minor")
    