import csv
import subprocess
import os
userPath=os.path.abspath(os.getcwd())

def importCSV():
    with open(fr"{userPath}\input.csv",'r') as file:
        return list(csv.reader(file))

def exportCSV(list,rows,columns):
    with open(fr"{userPath}\output.csv",'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in range(0, rows):
            csvwriter.writerow(list[i])

def editCSV():
    subprocess.Popen(['notepad.exe',fr"{userPath}\input.csv"])