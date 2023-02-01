import iomatrix

class Matrix:
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.data = []
        self.verify = False

    #imports matrix from CSV, verifies consistent row lengths, and verifies only numeric data
    def importMatrix(self):
        self.data.clear()
        csvFile = iomatrix.importCSV()
        self.rows = len(csvFile)
        self.columns = len(csvFile[0])
        for i in range(len(csvFile)):
            # checks that the length of each row is congruent.
            if len(csvFile[i]) != len(csvFile[0]):
                self.data.clear()
                self.verify = False
                input(
                    "Error importing matrix. Please ensure that row dimensions are consistent.")
                return 0
        try:
            for i in range(self.rows):
                inputrow = [float(x) for x in csvFile[i]]
                self.data.append(inputrow)
            self.verify = True
        except:
            self.data.clear()
            self.verify = False
            input(
                "Error importing matrix. Please ensure that matrix data contains only numeric values.")

    #prints matrix if called from main menu
    def print(self):
        if not self.verify:
            return 0
        print(f"Matrix is size {self.rows}x{self.columns}\n\n")
        for i in range(self.rows):
            for j in range(self.columns):
                print(f"{round(self.data[i][j],2):g}", end="\t"),
            print("")
        print("\n")
        state = input(f"Press enter to continue.\n") == 'y'

    #prints steps to be used in the rref
    def printStep(self, string):
        print(chr(10)+string)
        for i in range(self.rows):
            for j in range(self.columns):
                print(f"{round(self.data[i][j],2):g}", end="\t"),
            print("")

    #performs rref on the matrix
    def rref1(self):
        # verify that the matrix holds legal data and dimmensions
        if not self.verify:
            return 0

        self.printStep(f"Begin with this {self.rows}x{self.columns} matrix:")

        # offset describes the horizontal displacement of the index used to check matrix coefficients
        offset = 0
        for column in range(0, self.columns):
            row = column-offset
            coefficient = self.data[row][column]

            # swap rows if the index coefficient is 0 by scanning rows below
            if coefficient == 0:
                for checkRowForNonZero in range(row, self.rows):
                    if self.data[checkRowForNonZero][column] != 0:
                        temp = self.data[row]
                        self.data[row] = self.data[checkRowForNonZero]
                        self.data[checkRowForNonZero] = temp
                        self.printStep(
                            f"Swap R{row+1} and R{checkRowForNonZero+1}:")
                        coefficient = self.data[row][column]
                        break
            # if no rows exist to swap with, go back to beginning of for loop.
            # Up the offset, so the column index increases but row index stays the same
            if coefficient == 0:
                offset = offset+1
                continue

            # divide rows to get a 1 coefficient
            # if coefficient = 1, there is no need to divide row by the index coefficeint.
            if coefficient != 1.0:
                self.data[row] = [self.data[row][i] /
                                  coefficient for i in range(0, self.columns)]
                for checkRowForNonZero in range(0, self.columns):
                    if self.data[row][checkRowForNonZero] == -0.00:
                        self.data[row][checkRowForNonZero] = 0.00
                self.printStep(f"Divide R{row+1} by {round(coefficient,2)}:")

            # subtract r1 * coefficient from each row to get a column of 0's
            for rowIterator in range(0, self.rows):
                if rowIterator == row:
                    continue  # do not subtract row from itself
                if self.data[rowIterator][column] == 0:
                    continue  # if index already equals zero, then this step is redundant
                coefficient = self.data[rowIterator][column]
                self.data[rowIterator] = [self.data[rowIterator][i] -
                                          self.data[row][i]*coefficient for i in range(0, self.columns)]
                self.printStep(
                    f"Subtract {round(coefficient,2)}*R{row+1} from R{rowIterator+1}:")

            if row+1 == self.rows:
                break

        self.printStep("RREF complete.")
        iomatrix.exportCSV(self.data, self.rows,
                           self.columns)  # export to file
        input("Press enter to return to the main menu.")
