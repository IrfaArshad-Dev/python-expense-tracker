
import math

total = 0          # accumulator: starts at 0, OUTSIDE the loop
count = 0          # how many expenses were entered

print("===== EXPENSE TRACKER =====")
print("Enter an expense amount, e.g. 100, 50, 20.")
print("Type 'quit' when you are done.\n")

while True:
    entry = input("Enter expense (or 'quit'): ").strip()

    # Kill switch: stop the loop
    if entry.lower() == "quit":
        break

    # Defense: convert text to a number safely
    try:
        new_expense = float(entry)
    except ValueError:
        print("Invalid input. Please enter a number like 100 or 25.50.\n")
        continue

    # Reject zero, negative, and non-finite values (like nan or inf)
    if not math.isfinite(new_expense) or new_expense <= 0:
        print("The amount must be a number greater than 0.\n")
        continue

    # Accumulator pattern
    total = total + new_expense
    count = count + 1
    print(f"Added {new_expense:.2f}. Running total: {total:.2f}\n")

print("\n===== SUMMARY =====")
print(f"Expenses entered: {count}")
print(f"Total Spent: {total:.2f}")