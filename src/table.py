import copy
from arm import *


class Table:
    """Instance of Table"""

    def __init__(self, cubes):
        """Constructor for the table"""
        self.arm = Arm()
        self.cubes = cubes

    def __str__(self, detailed=False):
        """str method for Table"""
        res = ""
        if detailed:
            res += "Table(\n\t" + str(self.arm)
            for cube in self.cubes:
                res += ",\n\t" + str(cube)

            res += "\n)"

        else:
            res += "-["
            if self.arm.isHolding():
                res += str(self.arm._holding.label)
            res += "]"

            for cube in self.cubes:
                if cube.onTable():
                    res += "\n|"
                    current = cube
                    while current != None:
                        res += str(current.label) + '|'
                        current = current._under

        return res

    def getCube(self, cube=None, label=None):
        """Get a cube from the table"""
        for c in self.cubes:
            if ((label != None and c.label == label)
                    or (cube != None and c == cube)):
                return c
        return None

    def clone(self):
        """Clone the table"""
        return copy.deepcopy(self)

    def __eq__(self, op):
        """Overload the '==' operator"""
        return (isinstance(op, Table)
                and self.arm == op.arm
                and self.cubes == op.cubes)

    def getSuccessors(self):
        """Get every possible successors of this state"""
        successors = []

        # Action of placing a cube on the table or on a cube
        if self.arm.isHolding():
            # Place the cube on another cube
            for cube in self.cubes:
                if cube.free:
                    newTable = self.clone()
                    newTable.arm.drop(newTable.getCube(cube=cube))
                    successors.append(newTable)

            # Place the cube on the table
            newTable = self.clone()
            newTable.arm.drop(None)
            successors.append(newTable)

        else:
            # Try to hold each free cubes
            for cube in self.cubes:
                if cube.free:
                    newTable = self.clone()
                    newTable.arm.hold(newTable.getCube(cube=cube))
                    successors.append(newTable)

        return successors

    @ staticmethod
    def getTableSubjectStart():
        """Get the starting table subject"""
        table = Table([Cube("A"), Cube("B"), Cube("C")])

        table.getCube(label="C").on = table.getCube(label="A")
        return table

    @ staticmethod
    def getTableSubjectGoal():
        """Get the goal table subject"""
        table = Table([Cube("A"), Cube("B"), Cube("C")])

        table.getCube(label="A").on = table.getCube(label="B")
        table.getCube(label="B").on = table.getCube(label="C")
        return table
