'''Write a program to display the multiplication table as below with a given range'''
start_table = int(input("Enter the starting table: "))
end_table = int(input("Enter the ending table: "))

for i in range(1, 11):
    for j in range(start_table, end_table + 1):
        result = j * i
        print(j, "*", i, "=", result, end="\t")
    print()