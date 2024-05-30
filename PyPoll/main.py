import os
import csv

totalVotes = 0
candidateVotes = {}
maxPercent = 0
winner = ""

csvPath = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')

with open(csvPath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    csvHeader = next(csvReader)

    for row in csvReader:
        totalVotes += 1
        if row[2] in candidateVotes:
            candidateVotes[row[2]][0] += 1
        else:
            candidateVotes[row[2]] = [1,0]
    print("Total Votes: ",totalVotes)
    for candidate in candidateVotes:
        candidateVotes[candidate][1] = round((float(candidateVotes[candidate][0])/totalVotes)*100,3)
        if candidateVotes[candidate][1] > maxPercent:
            winner = candidate
            maxPercent = candidateVotes[candidate][1]
        print(candidate,": ",candidateVotes[candidate][1],"% (",candidateVotes[candidate][0],")")
    print("Winner: ",winner)

txtPath = os.path.join('.', 'PyPoll', 'Resources', 'election_data.txt')

with open(txtPath, 'w') as txtFile:
    txtWriter = csv.writer(txtFile)
    txtWriter.writerow(["Total Votes: " + str(totalVotes)])
    for candidate in candidateVotes:
        txtWriter.writerow([str(candidate) + ": " + str(candidateVotes[candidate][1]) + "% (" + str(candidateVotes[candidate][0]) + ")"])
    txtWriter.writerow(["Winner: " + winner])