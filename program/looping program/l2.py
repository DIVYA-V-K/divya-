'''Write a program to display the factors of a given number.'''
number = int(input("Enter a number: "))

factors = []

for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)

print("Factors of", number, "are:", ", ".join(map(str, factors)))
