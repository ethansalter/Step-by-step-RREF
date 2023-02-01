import matrix as m
from copy import deepcopy
import iomatrix

#initializes a defult matrix
matrix = m.Matrix()

#prints 100 new lines in terminal to clear view
def clearScreen():
    print(f"{chr(10)*100}")

#clears screen, prints instructions
def homeScreen():
    clearScreen()
    print(f"MATRIX SOLVER")
    print(
f"""Enter '1' to edit matrix
Enter '2' to view matrix
Enter '3' to perform RREF
Enter 'q' to quit program
""")

#main loop
while True:
    homeScreen()
    code = input()

    if code == "1":
        clearScreen()
        iomatrix.editCSV()

    if code == '2':
        clearScreen()
        matrix.importMatrix()
        matrix.print()

    #create a copy of matrix instance to perform rref on it.
    #original matrix is unaffected.
    if code == '3':
        clearScreen()
        matrix.importMatrix()
        matrixrref = deepcopy(matrix)
        matrixrref.rref1()

    if code == 'q':
        break
