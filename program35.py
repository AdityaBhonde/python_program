items = input("enter the elements of list").split()
items = [int(x) for x in items]  # Convert to integers  , frist is not put this

even = []
odd = []
icnt = 0
 

while icnt <= len(items) :
    if  items[icnt] % 2 == 0 :
         even.append(items[icnt])
    else :
         odd.append(items[icnt])
    icnt +=1   
print(even)
print(odd)    
