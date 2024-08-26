import csv

header = [['model', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11', 'R12', 'R13', 'R14', 'R15', 'R16', 'R17', 'R18']]
#headerV =  [['model', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18']]

with open('model_databank.csv', 'w', newline='') as file:
    fileWriter = csv.writer(file)
    fileWriter.writerows(header)
    file.close

#with open('Vdatabank.csv', 'w', newline='') as file:
#    fileWriter = csv.writer(file)
#    fileWriter.writerows(headerV)
#    file.close


