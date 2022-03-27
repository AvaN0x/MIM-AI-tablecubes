from cube import Cube, CubeException


class ArmException(Exception):
    pass


class Arm:
    """Instance of Arm"""

    def __init__(self):
        """Constructor for Arm"""
        self._holding = None

    def __str__(self):
        """str method for Arm"""
        return "Arm(" + str(self._holding.label if self._holding != None else None) + ")"

    def isHolding(self):
        """Check if the arm is holding a cube"""
        return self._holding != None

    def hold(self, cube):
        """Hold a cube"""
        if (not self.isHolding()):
            if (isinstance(cube, Cube)):
                self._holding = cube
                self._holding.setOnArm()
            else:
                raise ArmException("Cannot hold something which is not a cube")
        else:
            raise ArmException("Arm is already holding a cube")

    def drop(self, dropOn=None):
        """Drop the cube on the table or on another cube"""
        if (self.isHolding()):
            try:
                # If .on raises an exception, it will be caught here and the arm will still be holding the cube
                self._holding.on = dropOn
                self._holding = None
            except CubeException as e:
                print(e)
        else:
            raise ArmException("Arm has nothing to drop")

    def draw(self):
        """Draw the arm"""
        if (self._holding == None):
            print("  ╷  ")
            print("┌─┴─┐")
            print("╵   ╵")
        else:
            print("  │  ")
            self._holding.draw()

    def __eq__(self, op):
        """Overload the '==' operator"""
        return (isinstance(op, Arm)
                and self._holding == op._holding)

    holding = property(None, hold, None, "I'm the 'holding' property.")
