transactions = []

# Collect 5 transaction values from user
for i in range(1, 6):
    amount = float(input(f"Enter transaction amount {i}: "))
    transactions.append(amount)

# Calculate highest transaction and average spend
largest_transaction = max(transactions)
average_spend = sum(transactions) / len(transactions)

# Output results
print("\n--- Summary ---")
print(f"Largest Transaction: ${largest_transaction:.2f}")
print(f"Average Spend: ${average_spend:.2f}")