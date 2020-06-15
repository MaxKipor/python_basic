kilometers = int(input("kilometers "))
target = int(input("enter a target "))
day = 1
while kilometers < target:
    print("%.d day : %.2f km"% (day,kilometers))
    dime = round(((kilometers*10)/100), 2)
    day+=1
    kilometers +=dime

print("On %.d day athlete will reach at least %.d km"%(day+1, target))
