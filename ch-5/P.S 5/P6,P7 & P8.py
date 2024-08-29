d = {}

name=input("Enter your name:")
lang= input ("Enter the language:")

d.update({name: lang})
name=input("Enter your name:")
lang= input ("Enter the language:")

d.update({name: lang})
name=input("Enter your name:")
lang= input ("Enter the language:")

d.update({name: lang})
name=input("Enter your name:")
lang= input ("Enter the language:")

d.update({name: lang})

print("Dictionary is:", d)

#FIRST RUN RESULT4

# Enter your name:madahv
# Enter the language:py
# Enter your name:shashnk
# Enter the language:c++
# Enter your name:adwitiya
# Enter the language:backaiti
# Enter your name:rohan
# Enter the language:c
# Dictionary is: {'madahv': 'py', 'shashnk': 'c++', 'adwitiya': 'backaiti', 'rohan': 'c'}
# ------------------------------------------------------------------------------------------
#SECOND RUN RESULT 
# if two key are same 

# Enter your name:madhav
# Enter the language:py
# Enter your name:shashank
# Enter the language:c++
# Enter your name:adwitiya
# Enter the language:bakaiti
# Enter your name:shashank
# Enter the language:python 
# Dictionary is: {'madhav': 'py', 'shashank': 'python', 'adwitiya': 'bakaiti'}

#The <.update> method will update the data to the latest key and value pair
# ------------------------------------------------------------------------------------------
# THIRD RUN RESULT
# if two values are same

# Enter your name:madahv
# Enter the language:py
# Enter your name:shashank
# Enter the language:py
# Enter your name:genghis
# Enter the language:alpha
# Enter your name:beta
# Enter the language:sigma
# Dictionary is: {'madahv': 'py', 'shashank': 'py', 'genghis': 'alpha', 'beta': 'sigma'}