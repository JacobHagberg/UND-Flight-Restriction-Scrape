import openpyxl
import json

file = open('FlightRestrictions.json')
FlightData = json.load(file)

FlightRestrictionOrder = ['Closed', 'No Fly', 'No Dispatch', 'Dual Local Only', 'Dual Only', 'Solos Per METAR', 'Open']

#what to compare

YearInterval = [2023, 2023] #intervals of time to be included in the spreadsheet
MonthInterval = [3, 3]
DayInterval = [10, 20]
HourInterval = [0, 23]
FinalData = []
for i in range(24):
    FinalData.append([i, [0,0,0,0,0,0,0]])  #make sure that this gets updated with the length of FlightRestrictionOrder
previousDate = FlightData[0][0][0:4]
FlightRestrictStore = []

for i in range(0, len(FlightData) - 1):
    if FlightData[i][0][0:4] == previousDate:
        print('DateChecked')
        #print(FlightData[i][0][0])
        #print(YearInterval[0])
        if FlightData[i][0][0] >= YearInterval[0] and FlightData[i][0][0] <= YearInterval[1]: #timestamp year
            print('1')
            if FlightData[i][0][1] >= MonthInterval[0] and FlightData[i][0][1] <= MonthInterval[1]:
                print('2')
                if FlightData[i][0][2] >= DayInterval[0] and FlightData[i][0][2] <= DayInterval[1]:
                    print('3')
                    if FlightData[i][0][3] >= HourInterval[0] and FlightData[i][0][3] <= HourInterval[1]:
                        print('4')
                        FlightRestrictStore.append(FlightData[i][1][0])
    else:
        print(FlightRestrictStore)
        WorstForHour = len(FlightRestrictionOrder) - 1#This is going to start as the index for the least restrictive flight restriction in FlightRestrictionOrder and will track the most restrictive for that hour
        for p in range(len(FlightRestrictStore)):
            for o in range(0, WorstForHour):
                if FlightRestrictStore[p].find(FlightRestrictionOrder[o]) != -1:
                    WorstForHour = o
                    break
        print(WorstForHour)
        FinalData[previousDate[3]][1][WorstForHour] += 1 #Store the worst flight restriction for that hour

        previousDate = FlightData[i][0][0:4]
        FlightRestrictStore = []
        if FlightData[i][0][0] >= YearInterval[0] and FlightData[i][0][0] <= YearInterval[1]: #timestamp year
            if FlightData[i][0][1] >= MonthInterval[0] and FlightData[i][0][1] <= MonthInterval[1]:
                if FlightData[i][0][2] >= DayInterval[0] and FlightData[i][0][2] <= DayInterval[1]:
                    if FlightData[i][0][3] >= HourInterval[0] and FlightData[i][0][3] <= HourInterval[1]:
                        FlightRestrictStore.append(FlightData[i][1][0])

print(FinalData)

wb = openpyxl.Workbook()
sheet = wb.active
for i in range(0, 23):
    for o in range(len(FinalData[i][1])):
        c1 = sheet.cell(row = i + 1, column = o + 1)
        c1.value = FinalData[i][1][o]

wb.save("Test.xlsx") 