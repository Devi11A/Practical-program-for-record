#ProgramBK for Simple Interest
principal = float(input("Enter the Amount Borrowed: "))
time = float(input("Enter the number of years: "))
rate = float(input("Enter the rate of interest: "))
SI = (principal * time * rate) /  100 #By 100 to as rate is in percentage
print("The simple interest is",SI)
