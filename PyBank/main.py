import os
import csv

totalMonths = 0
previousPeriod = 0
net = 0
avgChange = 0
maxIncrease = ['Month',0]
maxDecrease = ['Month',0]

csvPath = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv')

with open(csvPath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    csvHeader = next(csvReader)
    temp = next(csvReader)
    totalMonths += 1
    net += int(temp[1])
    previousPeriod = int(temp[1])
    for row in csvReader:
        totalMonths += 1
        net += int(row[1])
        avgChange += (int(row[1])-previousPeriod)
        if (int(row[1])-previousPeriod) > maxIncrease[1]:
            maxIncrease[0] = row[0]
            maxIncrease[1] = (int(row[1])-previousPeriod)
        elif (int(row[1])-previousPeriod) < maxDecrease[1]:
            maxDecrease[0] = row[0]
            maxDecrease[1] = (int(row[1])-previousPeriod)
        previousPeriod = int(row[1])
    avgChange /= (float(totalMonths) - 1)
    avgChange = round(avgChange,2)

print("Total Months: ",totalMonths,"\nNet Total: $",net,"\nAverage Change: $",avgChange,"\nGreatest Increase in Profits: ",maxIncrease[0]," ($",maxIncrease[1],")\nGreatest Decrease in Profits: ",maxDecrease[0]," ($",maxDecrease[1],")")

txtPath = os.path.join('.', 'PyBank', 'Resources', 'budget_data.txt')

with open(txtPath, 'w') as txtFile:
    txtWriter = csv.writer(txtFile)
    txtWriter.writerow(["Total Months: " + str(totalMonths)])
    txtWriter.writerow(["Net Total: $" + str(net)])
    txtWriter.writerow(["Average Change: $" + str(avgChange)])
    txtWriter.writerow(["Greatest Increase in Profits: " + str(maxIncrease[0]) + " ($" + str(maxIncrease[1]) + ")"])
    txtWriter.writerow(["Greatest Decrease in Profits: " + str(maxDecrease[0]) + " ($" + str(maxDecrease[1]) + ")"])
