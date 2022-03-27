from xmlrpc.client import boolean


class CubeException(Exception):
    pass


class Cube:
    """Instance of cube"""

    def __init__(self, label="?", on=None):
        self._on = on  # None is table or arm, Cube is another cube
        self._under = None  # Cube or None
        self._onArm = False  # True if cube is on the arm
        self._free = True  # True if cube is free
        self._label = label  # Label of the cube

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

    def getOn(self):
        """Getter for where the cube is on"""
        return self._on

    def setOn(self, on):
        """Setter for where the cube is on"""
        if (on == None or isinstance(on, Cube)):
            self._on = on
            self._onArm = False
            self.free = self._under == None
            if self._on != None:
                self._on.free = False
                self._on._under = self

        else:
            raise CubeException(
                "Cannot be on something which is not a cube or None")

    def setFree(self, free):
        """Setter for free"""
        if isinstance(free, boolean):
            self._free = free

    def setOnArm(self):
        """Set the cube as being on the arm"""
        if self.free:
            if self._on != None:
                self._on._under = None
                self._on.free = True
                self._on = None
            self._onArm = True
            self.free = False
            self._under = None
        else:
            raise CubeException(
                "Cannot put a cube on the arm if it is not free")

    def __str__(self):
        """str method for Cube"""
        res = "Cube(" + self._label
        if self.onTable():
            res += ", onTable"
        elif self._on != None:
            res += ", onCube(" + str(self._on.label) + ")"
        else:
            res += ", onArm"

        res += ", free: " + str(self._free)
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

    def __eq__(self, op):
        """Overload the '==' operator"""
        return (isinstance(op, Cube)
                and self._label == op.label
                and self._on == op._on
                and self._free == op._free
                and self._onArm == op._onArm)

    on = property(getOn, setOn, None, "I'm the 'on' property.")
    under = property(None, None, None, "I'm the 'under' property.")
    onArm = property(None, None, None, "I'm the 'onArm' property.")
    free = property(isFree, setFree, None, "I'm the 'free' property.")
    label = property(getLabel, None, None, "I'm the 'label' property.")
