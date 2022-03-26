from node import Node


class astarNode(Node):
    """Class node representing a node from a tree for A*"""

    def __init__(self, value=None, childrens=None, parent=None, position=None):
        super().__init__(value, childrens, parent)
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def valueStr(self):
        """Return the value of the node as a string"""
        return super().valueStr() + ", position=" + str(self.position) + ", g=" + str(self.g) + ", h=" + str(self.h) + ", f=" + str(self.f)

    def __eq__(self, op):
        return self.position == op.position


def astar(funcHeuristic, funcCost, start, goal):
    """Apply a* algorithm to solve the tables"""
    # TODO: implement a* algorithm
    pass
