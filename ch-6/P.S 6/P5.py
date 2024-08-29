l = ['shashank','divya','rohan','ahmed','farooq']

name = input('Enter your name: ')
if (name in l):
    print('shashank is present in the list')
else: 
    print('Name not found in the list')
    enlist=input('Enter your name to enlist:')
    if (name == enlist):
       l.append(enlist)
       print('Name added to the list')
    elif (name != enlist):
        print('Name didn\'t match')

print(l)