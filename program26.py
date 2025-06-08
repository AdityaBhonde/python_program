Range = int(input("the the limit for printing the Fibonacci :"))

inta = 0
intb = 1
print(inta)
print(intb)
icnt = 1

while icnt <= Range :
    next = inta + intb
    print(next)
    inta = intb
    intb = next
    icnt +=1



