p1='Make a lot of money'
p2='subscribe to my channel'
p3='click this'
p4='buy now'
p5='easy money'

comment= input("Enter your comment: ")

if((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment) or (p5 in comment)):
    print('this comment is a spam!')
    
else:
    print('This comment is not a spam!')