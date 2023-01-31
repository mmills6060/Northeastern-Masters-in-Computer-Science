def calculateSalary(base, percentSales = .2):
    totalSales = 0
    salesAmount = float(input("Enter the sales amount of -1 to quit --> "))
    while(salesAmount != -1):
        totalSales += salesAmount
        salesAmount = float(input("Enter the sales amount or -1 to quit --> "))
    salary = base + percentSales*totalSales
    print("You made $" + str(round(salary, 2)))
    
calculateSalary(200)