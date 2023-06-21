'''Write a program to display the multiplication table as below with a given range
Sample Input
Start Table : 5
End Table: '''
start_table = int(input("Enter the starting table: "))
end_table = int(input("Enter the ending table: "))

for i in range(1, 11):
    for j in range(start_table, end_table + 1):
        if j >= i:
            result = j * i
            print(j, "*", i, "=", result)
    print()