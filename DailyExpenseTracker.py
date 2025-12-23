expenses=[]
for i in range(7):
    amount=float(input(f"Enter expense for day{i+1}:"))
    expenses.append(amount)
    total=sum(expenses)
    average=total/ len(expenses)
    highest=max(expenses)
    lowest=min(expenses)
    day_highest=expenses.index(highest)+1
    day_lowest=expenses.index(lowest)+1
print("/n-----Expense Report-----")
print(f"Total:KES{total}")
print(f"Average Daily Expenses:KES{average:2f}")
print(f"Highest Expenses:KES{highest} on Day{day_highest}")
print(f"Lowest Expenses:KES{lowest} on Day{day_lowest}") 
  
    