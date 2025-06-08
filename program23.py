iNo = int(input("Enter the number: "))
icnt = 2
isPrime = True  # Assume number is prime initially

if iNo < 0:
    iNo = -iNo

if iNo < 2:
    isPrime = False
else:
    while icnt <= iNo // 2:
        if iNo % icnt == 0:
            isPrime = False
            break
        icnt += 1

# Final output
if isPrime:
    print("The number is prime")
    print(True)
else:
    print("The number is non-prime")
    print(False)
