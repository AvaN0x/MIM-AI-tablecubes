class CubeException(Exception):
    pass


class Cube:
    """Instance of cube"""

    def __init__(self, label="?", on=None):
        self.on = on  # None is table, Cube is another cube, else would be the robotic arm
        self.onArm = False
        self.label = label

    def onTable(self):
        """Check if the cube is on the table"""
        return not self.onArm and self.on == None

    def onCube(self, cube):
        """"Check if the cube is on another cube"""
        # If the arg is a Cube, and the actually saved self.on is a cube, check if they are equals
        return (not self.onArm
                and isinstance(cube, Cube)
                and isinstance(self.on, Cube)
                and self.on == cube)

    def setOn(self, on):
        """Setter for where the cube is on"""
        if (on == None or isinstance(on, Cube)):
            self.on = on
        else:
            raise CubeException(
                "Cannot be on something which is not a cube or None")

    def __str__(self):
        """str method for Cube"""
        res = "Cube(" + self.label
        if self.onTable():
            res += ", onTable"
        elif isinstance(self.on, Cube):
            res += ", onCube(" + self.on.label + ")"

        res += ")"
        return res
