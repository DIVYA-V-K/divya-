name=input("enter a name")
gen= input("enter a gender (M/F)")
age= int(input("enter a age"))
days=int(input("enter a total number of working days"))

if   age>=18 and age<=30 and gen=='M':
    print("wage=  ",days*700)
elif age>=18 and age<=30 and gen=='F':
    print("wage=  ",days*750)
elif age>=30 and  age<=40 and gen=='M':
    print("wage ",days*800)
elif age>=30 and age<=40 and gen=='F':
    print("wage = ",days*850)
else:
    print("INVALID")     