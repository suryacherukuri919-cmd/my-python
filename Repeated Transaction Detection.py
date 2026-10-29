transactions = [500, 200, 500, 300, 200]

for amount in set(transactions):
    if transactions.count(amount) > 1:
        print("Duplicate:", amount)
