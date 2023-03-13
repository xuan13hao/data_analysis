# import numpy as np
# import pandas as pd
 
# txt = np.loadtxt('/home/xuan/TableFam489.hg38_multianno.txt')
# txtDF = pd.DataFrame(txt)
# txtDF.to_csv('file.csv',index=False)



import csv
import pandas as pd


def writeToCSV(filename, csvfilename):
    file = open(filename, "r")
    lines = list(file)
    with open(csvfilename, "w") as writeFile:
        writer = csv.writer(writeFile)
        for line in lines:
            words = line.strip().split(' ')
            words = filter(lambda x: len(x) > 0, words)
            words = list(words)
            writer.writerow(words)
    writeFile.close()
    file.close()


def readFromCSV(csvfilename):
    with open(csvfilename, "r") as readFile:
        reader = csv.reader(readFile)
        datas = list(reader)
        for data in datas:
            print(data)

def readFromCSVPandas(csvfilename):
    data = pd.read_csv('people.csv', error_bad_lines=False)
    print(data)

if __name__ == '__main__':
    writeToCSV('/home/xuan/TableFam489.hg38_multianno.txt','test.csv')
    #readFromCSV('people.csv')
    #readFromCSVPandas('people.csv')