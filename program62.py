def Reverse_Digit(iNo) :
    iDigit = 0
    iRev = 0
    while iNo != 0 :
      iDigit = iNo % 10
      iRev = iRev * 10 + iDigit
      iNo = iNo // 10

    print(iRev)







ivalue = int(input("Enter the number :"))

Reverse_Digit(ivalue)