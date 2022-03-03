from cube import *


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
            if (isinstance(cube, Cube)):
                self.__holding = cube
            else:
                raise ArmException(
                    "Cannot hold something which is not a cube")
        else:
            raise ArmException(
                "Arm is already holding a cube")

    def drop(self, dropOn=None):
        if (self.isHolding()):
            try:
                self.__holding.on(dropOn)
                self.__holding = None
            except CubeException as e:
                print(e)
        else:
            raise ArmException(
                "Arm has nothing to drop")
