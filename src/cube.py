from xmlrpc.client import boolean


class CubeException(Exception):
    pass


class Cube:
    """Instance of cube"""

    def __init__(self, label="?", on=None):
        self._on = on  # None is table, Cube is another cube, else would be the robotic arm
        self._onArm = False
        self._free = True
        self._label = label

    def getLabel(self):
        """Getter for label"""
        return self._label

    def onTable(self):
        """Check if the cube is on the table"""
        return not self._onArm and self._on == None

    def isFree(self):
        """Check if the cube is free"""
        return self._free

    def onCube(self, cube):
        """Check if the cube is on another cube"""
        # If the arg is a Cube, and the actually saved self._on is a cube, check if they are equals
        return (not self._onArm
                and isinstance(cube, Cube)
                and isinstance(self._on, Cube)
                and self._on == cube)

    def setOn(self, on):
        """Setter for where the cube is on"""
        if (on == None or isinstance(on, Cube)):
            self._on = on
            on.setFree(False)
        else:
            raise CubeException(
                "Cannot be on something which is not a cube or None")

    def setFree(self, free):
        """Setter for free"""
        if (isinstance(free, boolean)):
            self._free = free

    def setOnArm(self):
        """Set the cube as being on the arm"""
        self._on = None
        self._onArm = True
        self._free = False

    def __str__(self):
        """str method for Cube"""
        res = "Cube(" + self._label
        if self.onTable():
            res += ", onTable"
        elif isinstance(self._on, Cube):
            res += ", onCube(" + self._on.label + ")"

        res += ", free : " + str(self.isFree())
        res += ")"
        return res

    def draw(self):
        """Draw the cube"""
        # Draw first line
        if (not self._free and not self._onArm):
            print("├───┤")
        else:
            print("┌───┐")

        print("│ " + self._label + " │")

        if (self._on == None):
            print("└───┘")

    on = property(None, setOn, None, "I'm the 'on' property.")
    onArm = property(None, None, None, "I'm the 'onArm' property.")
    free = property(isFree, setFree, None, "I'm the 'free' property.")
    label = property(getLabel, None, None, "I'm the 'label' property.")
