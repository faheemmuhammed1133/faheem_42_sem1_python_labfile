#wap that defines a list of countries that are a member of BRICS and check whether a country is a member of BRICS or not.
brics=["BRAZIL","RUSIIA","INDIA","CHINA","SOUTH AFRICA"]
a=input("Enter a country: ").upper()
if a in brics:
    print(a,"is a member of BRICS")
else:
    print(a,"is not a member of BRICS")
