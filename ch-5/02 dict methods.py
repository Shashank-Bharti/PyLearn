marks = {
    'Shashank':100,
    'abhilash':20,
    'pratigya':65,
    'ronak':90,
    0:"shashi"
}

print(marks.items())
print(marks.keys())
print(marks.values())

# marks.update({'abhilash':25,'shashank':99})
# print(marks)

# print(marks.get('ronak2')) #gives none
# print(marks['ronak2'])#returns error

# marks.clear() #clears the dict
# print(marks)

# new_dict = dict.fromkeys(marks,0) #Make a new dictionary with old dictionary keys and values as 0
# print(new_dict)


# marks.pop('abhilash') #Pops an item from the dictionary
# print(marks)

# print(marks.popitem()) #Removes the last(key, value) pair as a tuple from the dictionary
# print(marks)
