def clearScreen():
    print(f"{chr(10)*10}")

class Matrix:
    def __init__(self, name, rows, columns):
        self.name = name
        self.rows = rows
        self.columns = columns
        self.data = []

    def verifySize(self):
        if self.rows == 0 or self.columns == 0:
            input(f"Matrix has not been initialized. Please define a valid size before using this option.\n")
            return True
        else:
            return False

    def verifyData(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if not isinstance(self.data[i][j], float):
                    # Fail, contains * characters
                    input("Matrix contains non float type characters. Please edit matrix data before using this option.")
                    return True
        return False

    def editSize(self):
        clearScreen()
        self.data.clear()
        while True:
            self.rows = input("How many rows?\n")
            if self.rows.isdigit():
                self.rows = int(self.rows)
                break
            print("Number of rows must be an integer value. Please try again.")
        while True:
            self.columns = input("How many columns?\n")
            if self.columns.isdigit():
                self.columns = int(self.columns)
                break
            print("Number of columns must be an integer value. Please try again.")

        for i in range(self.rows):
            inputrow = ['*']*self.columns
            self.data.append(inputrow)


    def editData(self):
        if self.verifySize():
            return 0       
        
        while True:
            clearScreen()
            code = input(
            f"Enter '1' to input new data\nEnter '2' to edit data row\nEnter '3' to edit data point\nEnter 'q' to go back\n")
            if code == "1":
                self.editAllData()
                return 0
            if code == '2':
                self.editDataRow()
                return 0
            if code == '3':
                self.editDataPoint()
                return 0
            if code == 'q':
                return 0


    def editAllData(self):
        clearScreen()
        print(f"Matrix is size {self.rows}x{self.columns}")
        for i in range(self.rows):
            while True:
                inputrow = input("Input data for row " + str(i+1)+" (delineate with spaces):\n")
                if inputrow.count(' ') == self.columns-1:
                    inputrowlist=inputrow.split(' ')
                    break
                elif inputrow == "":
                    return 0
                elif inputrow.count(' ') < self.columns-1:
                    print("Dimensional error. Too few inputs given. Please try again.")
                elif inputrow.count(' ') > self.columns-1:
                    print("Dimensional error. Too many inputs given. Please try again")
            for j in range(self.columns):
                try: self.data[i][j] = float(inputrowlist[j])
                except: input("Error handling data. Please make sure data is type 'float'")

    def editDataRow(self):
        clearScreen()
        while True:
            row = int(input(f"Which row? (1-{self.rows})\n"))
            if row < self.rows+1 and row > 0:
                break
            print("Please enter a valid row.\n")
        while True:
            print(f"Matrix is size {self.rows}x{self.columns}")
            inputrow = input("Input data for row " + str(row)+" (delineate with spaces):\n")
            if inputrow.count(' ') == self.columns-1:
                inputrowlist=inputrow.split(' ')
                break
            print("Please try again.")
        for j in range(self.columns):
            try: self.data[row-1][j] = float(inputrowlist[j])
            except: input("Error handling data. Please make sure data is type 'float'")

    def editDataPoint(self):
        clearScreen()
        while True:
            row = int(input(f"Which row? (1-{self.rows})\n"))
            if row < self.rows+1 and row > 0:
                break
            print("Please enter a valid row.\n")
        while True:
            column = int(input(f"Which column? (1-{self.columns})\n"))
            if column < self.columns+1 and column >0:
                break
            print("Please enter a valid column.\n")
        try: self.data[row-1][column-1] = float(input(f"New value? (currently '{self.data[row-1][column-1]}')\n"))
        except: input("Error handling data. Please make sure data is type 'float'")

    def print(self):
        clearScreen()
        if self.verifySize():
            return 0
        print(f"Matrix is size {self.rows}x{self.columns}\n\n")

        for i in range(self.rows):
            for j in range(self.columns):
                print(str(self.data[i][j]), end="\t"),
            print("")
        print("\n")
        state = input(f"Press enter to continue.\n") == 'y'

    def rref(self):
        if self.verifySize():
            return 0
        if self.verifyData():
            return 0
