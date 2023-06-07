def calculate_tip():
    food_rating = int(input("enter the food rating(1-5)"))
    service_rating = int(input("enter the service rating (1-5)"))
    ambience_rating = int(input("enter the ambience rating(1-5)"))
    bill_amount = float(input("enter the bill amount")) 
if food_rating >= 4 and service_rating >= 4 and ambience_rating >=4:
    tip_ercentage 0.1
elif food_rating >=3 and service_rating >=3 and ambience_rating >=3: 
    tip_percentage = 0.05
elif food_rating >= 3:
    tip_percentage = 0.05
else:
    tip_percentage = 0.01
tip_amount = bill_amount * tip_percentage
total_amount = bill_amount + tip_amount  
print("bill amount :",bill_amount)
print("tip amount :",tip_amount)
print("total amount :",total_amount)