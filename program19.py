hours1 = int(input("enter the hours1 :"))
minutes1 = int(input("enter the minutes1 :"))
sec1 = int(input("enter the sec1 :"))

timestamp1 = (hours1 * 3600) + (minutes1 * 60) + (sec1)
print(timestamp1)

hours2 = int(input("enter the hours2 :"))
minutes2 = int(input("enter the minutes2 :"))
sec2 = int(input("enter the sec2 :"))

timestamp2 = (hours2 * 3600) + (minutes2 * 60) + (sec2)
print(timestamp2)

icout = 0
if timestamp1 > timestamp2 :
    
    icount = timestamp1 - timestamp2
    print(str(icount)+"timestamp1 - timestamp2")
else :
    
    icount = timestamp2 - timestamp1 
    print(str(icount)+"timestamp2 - timestamp1")