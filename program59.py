def Sum_Digit(iNo) :
    idigit = 0
    iSum = 0
    while iNo != 0 :
        idigit = iNo % 10
        iSum = iSum + idigit
        iNo = iNo // 10

    print(str(iSum)+" : is the sum of the digit")    


    






ivalue = int(input("Enter the number : "))

Sum_Digit(ivalue)