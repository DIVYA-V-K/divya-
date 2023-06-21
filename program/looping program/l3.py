'''Write a program to display the prime in the given range. '''
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

prime_numbers = []

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

print("Prime numbers in the range", start, "to", end, "are:", ", ".join(map(str, prime_numbers)))