def PrintFactors(iNo):
    icnt = 1
    if iNo < 0:
        iNo = -iNo
    while icnt <= (iNo // 2):
        if (iNo % icnt) == 0:
            print(icnt)
        icnt += 1
    

iValue = int(input("Enter the number: "))
PrintFactors(iValue)
          

          