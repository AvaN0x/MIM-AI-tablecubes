from cube import Cube


class ArmException(Exception):
    pass


class Arm:
    def __init__(self):
        self.__holding = None

    def __str__(self):
        return "Bras tient : " + str(self.__holding)

    def isHolding(self):
        return self.__holding != None

    def hold(self, cube):
        if (not self.isHolding()):
            if (cube == None or isinstance(cube, Cube)):
                self.__holding = cube
            else:
                raise ArmException(
                    "Cannot hold something which is not a cube or None")
        else:
            raise ArmException("Arm is already holding a cube")
