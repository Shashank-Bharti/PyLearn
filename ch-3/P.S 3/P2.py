name= input('What is your name?')

from datetime import date

today=date.today()

letter= '''Dear <|NAME|>,
You are selected!
<|DATE|>'''

print(letter.replace("<|NAME|>",name).replace("<|DATE|>", str(today)))