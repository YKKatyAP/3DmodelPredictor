import csv

finalList = []
header = ['model']
#headerV =  [['model', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18']]
r = 1

while r < 39:
    ratiohead = "R" + str(r)
    header.append(ratiohead)
    r = r + 1 

finalList.append(header)

with open('model_databank.csv', 'w', newline='') as file:
    fileWriter = csv.writer(file)
    fileWriter.writerows(finalList)
    file.close

