'''Write a program to display the Amstrong numbers in the given range'''
lower_range = int(input("Enter lower range: "))
upper_range = int(input("Enter upper range: "))

armstrong_numbers = []

for num in range(lower_range, upper_range + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        armstrong_numbers.append(num)

print("The Armstrong numbers are:")
for armstrong in armstrong_numbers:
    print(armstrong)