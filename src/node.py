from anytree import Node as ATNode, RenderTree as ATRenderTree  # pip install anytree
from anytree.exporter import UniqueDotExporter


class Node:
    """Class node representing a node from a tree"""

    def __init__(self, value=None, childrens=None, parent=None):
        """Constructor of this node, default values for value and nodes are None"""
        self.depth = 0
        if parent != None:
            parent.childrens.addChild(self)
        self.value = value
        self.childrens = childrens
        # Set parent of each child
        if self.childrens != None:
            for node in self.childrens:
                node.setParent(self)

    def setParent(self, parent):
        """Set parent of a node"""
        self.parent = parent
        self.setDepth(self.depth + 1)

    def setDepth(self, depth):
        """Set the depth of the node"""
        self.depth = depth
        if self.childrens != None:
            for node in self.childrens:
                node.setDepth(self.depth + 1)

    def addChild(self, node):
        """Add a node to the childrens"""
        if self.childrens == None:
            self.childrens = []
        self.childrens.append(node)
        node.setParent(self)

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

    def valueStr(self):
        """Return the value of the node as a string"""
        return str(self.value)

    def draw(self, dot=False, dotFileName=None, nodenamefunc=None, nodeattrfunc=None):
        """Draw the tree using AnyTree RenderTree or DotExporter"""
        if dot:
            UniqueDotExporter(self.getAnyTreeNode(), nodenamefunc=nodenamefunc, nodeattrfunc=nodeattrfunc).to_picture(
                dotFileName if dotFileName != None else "tree.png")

        else:
            # Code taken from the documentation
            for pre, fill, node in ATRenderTree(self.getAnyTreeNode()):
                print("%s%s" % (pre, node.name))

    def getAnyTreeNode(self, parent=None):
        """Recursive call to create a tree for AnyTree"""
        # If we don't have a parent, then this node is the parent
        if parent == None:
            node = ATNode(self.valueStr())
        else:
            node = ATNode(self.valueStr(), parent=parent)

        # Recursive call to create childrens
        if self.childrens != None:
            for childnode in self.childrens:
                childnode.getAnyTreeNode(node)
        return node
