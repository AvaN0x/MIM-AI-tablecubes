class Node:
    """Class node representing a node from a tree"""

    def __init__(self, value=None, childrens=None, parent=None):
        """Constructor of this node, default values for value and nodes are None"""
        self.parent = parent
        self.value = value
        self.childrens = childrens
        # Set parent of each child
        if self.childrens != None:
            for node in self.childrens:
                node.setParent(self)

    def setParent(self, parent):
        """Set parent of a node"""
        self.parent = parent

    def addNode(self, node):
        """Add a node to the childrens"""
        self.childrens.append(node)

    def __str__(self, t=0):
        """Recursive str method for the node"""
        res = t * "  " + "Node(" + str(self.value)

        # Only iterate through childrens if they are not None
        if self.childrens != None:
            res += ", "
            # first is used to only display ", " between each elements
            first = True
            for node in self.childrens:
                if first:
                    first = False
                else:
                    res += ", "

                res += "\n" + t * "  "
                res += node.__str__(t + 1)  # Recursive call
            res += "\n" + t * "  "

        res += ")"
        return res

