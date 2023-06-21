'''Write a program to display the count of even and odd numbers in a given range.'''
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

even_count = 0
odd_count = 0

for num in range(start, end + 1):
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even:", even_count)
print("Odd:", odd_count)