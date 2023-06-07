fare = 1020
discount = 20/100
age = int(input("enter the passenger age"))
if age > 60:
    discounted_fare =fare-(fare*discount)
    print("the discounted fare for senior citizen is Rs",discounted_fare)
else:
    print("no discount is applicable.the fare is Rs",fare)