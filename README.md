# 💰 Expense Tracker (Python)

A console Expense Tracker built in Python as **Project 2** of my Python Programming Internship at Decode Labs.

The user enters expense amounts one by one. The program adds them up and shows the **Total Spent**.

## ✨ Features
- ➕ Enter any number of expenses (whole numbers or decimals, e.g. `100` or `25.50`)
- 📈 Shows the running total after every entry
- 🛑 Type `quit` to stop and see the final summary (number of expenses and total spent)
- 🛡️ Input validation: text like `ten`, empty input, zero, negative numbers, and `nan`/`inf` are rejected without crashing

## 🧠 Concepts Practised
- **Accumulator pattern:** `total = total + new_expense`
- **State:** `total` is created *outside* the loop so it keeps its value
- **`while True` loop** with `break` as a "kill switch"
- **Defensive coding:** `try / except ValueError` when converting input to a number
- **Type conversion:** `float()` so `"100" + "50"` does not become `"10050"`
- **Formatted output** with f-strings (`:.2f`)

## ▶️ How to Run
```bash
python expense_tracker.py
```
Requires Python 3. No extra libraries needed.

## 📸 Example
```
Enter expense (or 'quit'): 100
Added 100.00. Running total: 100.00

Enter expense (or 'quit'): ten
Invalid input. Please enter a number like 100 or 25.50.

Enter expense (or 'quit'): 50
Added 50.00. Running total: 150.00

Enter expense (or 'quit'): quit

===== SUMMARY =====
Expenses entered: 2
Total Spent: 150.00
```

## 🚀 Possible Next Steps
- Save expenses to a file
- Add expense categories (food, transport, etc.)
- Show the highest and average expense

## 👩‍💻 Author
**Irfa Arshad** | [GitHub](https://github.com/IrfaArshad-Dev)

*Built during the Decode Labs Python Programming Internship (Oct to Nov 2026).*
