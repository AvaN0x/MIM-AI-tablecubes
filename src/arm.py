from cube import Cube, CubeException


class ArmException(Exception):
    pass


class Arm:
    def __init__(self):
        self._holding = None

    def __str__(self):
        return "Arm(" + str(self._holding) + ")"

    def isHolding(self):
        return self._holding != None

    def hold(self, cube):
        if (not self.isHolding()):
            if (isinstance(cube, Cube)):
                self._holding = cube
                cube.setOnArm()
            else:
                raise ArmException("Cannot hold something which is not a cube")
        else:
            raise ArmException("Arm is already holding a cube")

    def drop(self, dropOn=None):
        if (self.isHolding()):
            try:
                self._holding.on(dropOn)
                self._holding = None
            except CubeException as e:
                print(e)
        else:
            raise ArmException("Arm has nothing to drop")

    holding = property(None, hold, None, "I'm the 'holding' property.")
