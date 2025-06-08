s = input("Enter a string: ")

i = 0
result = ""   # result is defult set to ""

while i < len(s):      # len(s)  this is the in build  function to calcute the string
    if i % 3 != 0:
        result += s[i]
    i += 1  # i++ in c 

print("Resulting string:", result)
