import copy
from arm import *


class Table:
    """Instance of Table"""

    def __init__(self, cubeA, cubeB, cubeC):
        """Constructor for the table"""
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

    def clone(self):
        """Clone the table"""
        return copy.deepcopy(self)

    def __eq__(self, op):
        """Overload the '==' operator"""
        return (isinstance(op, Table)
                and self.arm == op.arm
                and self.A == op.A
                and self.B == op.B
                and self.C == op.C)

    @ staticmethod
    def getTableSubjectStart():
        """Get the starting table subject"""
        table = Table(Cube("A"), Cube("B"), Cube("C"))

        table.C.on = table.A
        return table

    @ staticmethod
    def getTableSubjectGoal():
        """Get the goal table subject"""
        table = Table(Cube("A"), Cube("B"), Cube("C"))

        table.A.on = table.B
        table.B.on = table.C
        return table
