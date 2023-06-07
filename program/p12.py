salary = float(input("enter the salary of he employee"))
years_of_service = int(input("enter he year of service"))
if years_of_service > 10:
    bonus_percentage = 0.1  # 10% bonus
elif years_of_service >6:
    bonus_percentage = 0.08   # 8% bonus
else:
    bonus_percentage = 0.05    # 5% bonus
bonus = salary * bonus_percentage
print("the bonus for the employee is:",bonus)