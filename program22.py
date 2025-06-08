iNo = int(input("Enter the number"))
iRev = 0

while iNo != 0 :
    iDigit = iNo % 10 
    iRev = iRev * 10 + iDigit 
    iNo = iNo // 10  # if we divide by / it will get float value , so for the integer return we use //
print(iRev)    