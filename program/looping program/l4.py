'''Write a program to display the multiplication table as below '''
number = int(input("Enter a number: "))

for i in range(1, 11):
    result = number * i
    print(number, "*", i, "=", result)