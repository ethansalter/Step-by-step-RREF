import matrix as m

matrix = m.Matrix("Ethan", 0, 0)

while True:
    m.clearScreen()
    print(f"MATRIX SOLVER")

    code = input(
        f"Enter '1' to define size\nEnter '2' to edit data\nEnter '3' to view matrix\nEnter '4' to perform RREF\n")
    if code == "1":
        matrix.editSize()
    if code == '2':
        matrix.editData()
    if code == '3':
        matrix.print()
    if code == '4':
        matrix.rref()
