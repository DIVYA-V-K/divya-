side1=int(input("Enter value of side1:"))
side2=int(input("Enter value of side2:"))
side3=int(input("Enter value of side3:"))
if(side1+side2>side3 and side1+side3>side2 and side2+side3>side1):
   print("Triangle can be formed")
else:
   print("Triangle is not possible")