import csv
# EXTRACT FIRST ROW FROM CSV FILE 
# VERIFY IF THE FILE IN PARAMS AS CSV FILE 
# IF TRUE THEN EXTRACT HEADER AND PUT IT IN LIST 
def GetCollumnFromFile(file):
    if verifyFileExtention(file) : 
        collumns = []
        with open(file,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ',')
            i = 0 
            for row in plots:
                if i == 0 :
                    for x in row : 
                        x = str(x).replace('ï»¿','')
                        collumns.append(x)
                    break 
        return collumns
    else: 
        return False 

## VERIFY FILE EXTENTION  
def verifyFileExtention(filename):
    if(filename[-4:] == '.csv'):
        return True
    else : 
        return False 
 
# this function verify if value existe in header or not 
# return true if value existe inheader
# return false if value not existe in header 
def verifyExist(header , value):
    if value in header:
        return True 
    else:
        return False 


def Compare2Headers(header1 , header2):
    HeaderColored1 = []
    HeaderColored2 = []
    exist=""
    for i in range(len(header1)):
        if header1[i] == header2[i]:
            exist = "true"
            print("header",header1[i],"some postion") 
        elif verifyExist(header1 , header2[i]):
            exist = "position"
            print("header",header1[i]," existe but with deffrent postion") 
        else:
            exist = "false"
            print("header",header1[i]," not existed ") 
        temporaryDict1 = {
                "value": header1[i],
                "exist": exist
                }
        temporaryDict2 = {
                "value": header2[i],
                "exist": exist
                }    
        HeaderColored1.append(temporaryDict1)
        HeaderColored2.append(temporaryDict2)
    return HeaderColored1 , HeaderColored2



## main ##


header1 = GetCollumnFromFile('exempleFile.csv')
header2 = GetCollumnFromFile('exempleFile2.csv')
if header1 == False or header2 == False : 
    print("Not CSV File")
else : 
    HeaderColored1 = Compare2Headers(header1  , header2)[0]
    print(HeaderColored1)
    HeaderColored2 = Compare2Headers(header1  , header2)[1]
    print(HeaderColored2)
 
"""headerLine="" 
for x in header1 : 
    headerLine += str(x).replace('ï»¿','')
"""