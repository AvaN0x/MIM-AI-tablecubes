from arm import *


class Table:
    """Instance of Table"""

    def __init__(self, cubeA, cubeB, cubeC):
        self.arm = Arm()
        self.A = cubeA
        self.B = cubeB
        self.C = cubeC

    def __str__(self):
        """str method for Table"""
        res = "Table(\n\t" + str(self.arm) + "\n\t"
        res += str(self.A) + "\n\t" + str(self.B) + \
            "\n\t" + str(self.C)
        # for cube in self.cubes:
        #     res += ",\n\t" + str(cube)

        res += "\n)"
        return res

    def draw(self):
        """Draw the state of the table"""
        if (self.A._free):
            self.A.draw()
            if (self.A.onCube(self.B)):
                self.B.draw()
                if (self.B.onCube(self.C)):
                    self.C.draw()
            if (self.A.onCube(self.C)):
                self.C.draw()
                if (self.C.onCube(self.B)):
                    self.B.draw()

        if (self.B._free):
            self.B.draw()
            if (self.B.onCube(self.A)):
                self.A.draw()
                if (self.A.onCube(self.C)):
                    self.C.draw()
            if (self.B.onCube(self.C)):
                self.C.draw()
                if (self.C.onCube(self.A)):
                    self.A.draw()

        if (self.C._free):
            self.C.draw()
            if (self.C.onCube(self.A)):
                self.A.draw()
                if (self.A.onCube(self.B)):
                    self.B.draw()
            if (self.C.onCube(self.B)):
                self.B.draw()
                if (self.B.onCube(self.A)):
                    self.A.draw()

        print()
        self.arm.draw()

    @ staticmethod
    def getTableSubject():
        """Get the table subject"""
        A = Cube("A")
        B = Cube("B")
        C = Cube("C")
        table = Table(A, B, C)
        # C.on = A
        # B.setOnArm()
        # table.arm._holding = B

        A.on = B
        B.on = C
        return table
