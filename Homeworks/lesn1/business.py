receipts = int(input("enter receipts : "))
spending = int(input("enter spending : "))
income = 0
loss = 0
if (receipts - spending) > 0:
    income = receipts - spending
    profitability = income/receipts
    employees = int(input("enter number of  employees : "))
    print("income = {0}, profitability = {1}, income on employee {2}".format(income, profitability, (income/employees)))
else:
    loss = spending - receipts
    print("loss = {0}".format(loss))



