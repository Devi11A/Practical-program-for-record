num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
num3 = int(input("Enter the number 3: "))
print("The numbers are",num1,num2,num3)
num1, num2, num3 = num2 + num3, num1 + num3, num1 + num2
print("After swapping with the sum of other 2 no:",num1,num2,num3)
