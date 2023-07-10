import csv 
def displayData(file,i):   
    with open(file,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',')
        for row in plots : 
            print(row[i])