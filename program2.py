# Swapping using a temporary variable
a = input("Enter value for a: ")
b = input("Enter value for b: ")

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)
