def Perfect_Squares(iLimit):
    icnt = 1
    ips = 0
    idigit = 0
    iSum = 0
    while True:
        ips = icnt * icnt
        if ips > iLimit:
            break
        print("this are all squares ")

        print(ips, " " )
        while ips != 0:
         idigit = ips % 10
         iSum = iSum + idigit
         ips = ips // 10
         icnt += 1
   
    if iSum < 10:
        print("this are sum less than 10 ")
        print(ips, " " )



ivalue = int(input("enter the limit: "))
Perfect_Squares(ivalue)

