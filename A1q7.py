d=int(input('Enter number of days='))
def find(d):
    years=int(d/365)
    d-=(years*365)
    month=int(d/30)
    d-=(month*30)
    week=int(d/7)
    d-=(week*7)
    print('Years=',years,'\nMonths=',month,'\nWeeks=',week,'\nDays=',d)


find(d)