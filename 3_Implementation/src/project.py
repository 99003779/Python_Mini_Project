# importing libraries for better and compact implementation of code

import pandas as pd

from openpyxl import load_workbook


class LogFile:

    # constructor initialization

    def __init__(self, filename):
        self.fileName = filename

    # read function has been defined

    def read(self, filename):
        df = pd.read_excel(filename, sheet_name=[0, 1, 2, 3, 4])
        return df



# child class inheriting the features of parent class
class PopulateExcel(LogFile):

    def save_in_master(self, filename, output):

        # load_workbook( ) function is used
        # when you have to access an MS Excel file in openpyxl module.
        # load workbook function only works if
        # you have an already created file on your disk
        # and you want to open workbook for some operation.

        book = load_workbook(filename)
        writer = pd.ExcelWriter(filename, engine='openpyxl', mode='a')
        writer.book = book

        # ExcelWriter for some reason uses
        # writer.sheets to access the sheet.
        # If you leave it empty it will not
        # know that sheet Main is already there
        # and will create a new sheet.

        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

        cols = []
        for j in range(len(output.columns)):
            cols.append(output.columns[j])

        output.to_excel(writer, "MasterSheet", columns=cols, index=False)

        writer.save()
class Summary(PopulateExcel):
    def save_summary(self, filename, summaryList):
        book = load_workbook(filename)
        writer = pd.ExcelWriter(filename, engine='openpyxl', mode='a')
        writer.book = book

        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

        SHEETLIST = []
        for j in range(len(summaryList)):
            SHEETLIST.append("Sheet" + str(j + 1))

        dcf = pd.concat(
            [pd.DataFrame(SHEETLIST, columns=['Sheet List']),
             pd.DataFrame(summaryList, columns=['Data Count'])],
            axis=1)

        dcf.to_excel(writer, "Summary", index=False)

        writer.save()


# object of class has been created
obj = Summary("DataSheet.xlsx")

# function of parent class has been called using object of child class
df = obj.read("DataSheet.xlsx")
print (df)
concatenatedOutput = pd.DataFrame()
summaryList = [0] * 5

while 1:
    regNo = int(input("Enter Registration Number: "))
    name = input("Enter Name: ")
    eMail = input("Enter Email ID: ")

    output = pd.DataFrame()
    times = 0

    for i in range(5):
        selectedRow = df[i].loc[
            (df[i]['Name '] == name) &
            (df[i]['Registration Number'] == regNo) &
            (df[i]['Email ID'] == eMail)]
        summaryList[i] = summaryList[i] + selectedRow.shape[0]

        if times == 0:
            output = pd.concat([output, selectedRow.iloc[:, 1:4]], axis=1)
            times = 1

        output = pd.concat([output, selectedRow.iloc[:, 4:]], axis=1)
    print(output)

    # obj.save("DataSheet.xlsx", output)
    concatenatedOutput = pd.concat([concatenatedOutput, output], axis=0)

    decision = input("Continue (y/n)? ")

    if decision == 'y':
        continue

    else:
        break

obj.save_in_master("DataSheet.xlsx", concatenatedOutput)

obj.save_summary("DataSheet.xlsx", summaryList)

print("Data has been printed to the mastersheet")

# Ali Adibi	99673798	ali.adibi@ece.gatech.edu

# Professor Peter Y. K. Cheung	99673786	p.cheung@imperial.ac.uk

# MOTANI, Mehul	99673808	elemm@nus.edu.sg

# SOH, Wee Seng	99673810	elesohws@nus.edu.sg

# Navid Asadi	99673813	nasadi@ufl.edu
