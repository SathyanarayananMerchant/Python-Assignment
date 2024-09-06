def calculator(a,b,op):
    if op=='add':
        print('Sum=',a+b)
    if op=='sub':
        print('Sub=',a-b)
    if op=='mul':
        print('Product=',a*b)
    if op=='div':
        print('Division=',a/b)
    
s=str(input('Calulator operation='))
a=int(input('1st num='))
b=int(input('2nd num='))
calculator(a,b,s)