from arm import *


class Table:
    """Instance of Table"""

    def __init__(self, cubes=[]):
        self.arm = Arm()
        self.cubes = cubes

    def __str__(self):
        """str method for Table"""
        res = "Table(\n\t" + str(self.arm)
        for cube in self.cubes:
            res += ",\n\t" + str(cube)

        res += "\n)"
        return res
