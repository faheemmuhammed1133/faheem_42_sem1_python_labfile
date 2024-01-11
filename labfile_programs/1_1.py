#WAP to compute simple interest for given Principal amount, time and rate of interest.
p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interest: "))
n=float(input("Enter tenor(in years): "))
si=(p*n*r)/100
print("Simple Interest:",si) 
print("total amount is:",si+p)