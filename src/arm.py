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
                print("L'objet a tenir n'est pas un cube !")
        else:
            print("Le bras tient déjà un objet !")
