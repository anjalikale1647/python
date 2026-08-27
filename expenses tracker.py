print("\n=*=*=*=*=* MONTHLY EXPENSES TRACKER *=*=*=*=*=")

expense_name = [""] * 10     
expense_value = [0] * 10

count = 0
total = 0

choice = "yes"

while choice == "yes":
    expense_name[count] = input("Enter expense name: ")
    expense_value[count] = float(input("Enter expense amount ($): "))

    total = total + expense_value[count]

    count = count + 1      

    choice = input("Add another expense? (yes/no): ").lower()

print("\nMonthly Expense")

for i in range(count):
    print(expense_name[i], "- $", expense_value[i])

print("Total Expenses: $", total)

