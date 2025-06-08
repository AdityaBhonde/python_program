iNo = int(input("enter the number"))
iDigit = 0
iSum = 0

while iNo != 0 :
    iDigit = iNo % 10
    iSum = iSum + iDigit
    iNo = iNo // 10 
print("the sum of the digits is "+str(iSum))    