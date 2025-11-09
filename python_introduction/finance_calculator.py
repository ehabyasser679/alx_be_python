MonthlyIncome = int(input("Enter your monthly income:"))
MonthlyExpenses = int(input("Enter your monthly expenses:"))
MonthlySavings = MonthlyIncome - MonthlyExpenses
print("Your monthly savings are", MonthlySavings)
ProjectedSavings = MonthlySavings * 12 + (MonthlySavings * 12 * 0.05)
print("Projected savings after one year, with interest, is:", ProjectedSavings)