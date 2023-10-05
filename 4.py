def leap(year):
    if(year%400==0 or (year%100!=0 and year%4==0)):
        return 1
    else:
        return 0    
