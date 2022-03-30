from node import Node


class AstarException(Exception):
    pass


class astarNode(Node):
    """Class node representing a node from a tree for A*"""

    def __init__(self, value=None, childrens=None, parent=None):
        super().__init__(value, childrens, parent)
        self.g = 0
        self.h = 0
        self.f = 0

    def valueStr(self):
        """Return the value of the node as a string"""
        return (super().valueStr() + "\ng=" + str(self.g) + ", h=" + str(self.h)).replace('\n', '\l')

    def __eq__(self, op):
        """Overload the '==' operator"""
        return op != None and self.value == op.value


def astar(funcHeuristic, funcCost, startValue, goalValue):
    """Apply a* algorithm to solve the tables"""
    root = astarNode(startValue)
    # Calculate heuristic, cost and f
    root.h = funcHeuristic(value=root.value, node=root)
    root.g = funcCost(value=root.value, node=root)
    root.f = root.g + root.h

    # Create the open and closed lists
    openedNodes = [root]
    closedNodes = []

    while len(openedNodes) > 0:
        # Get first node and remove it from the open list

        node = openedNodes.pop(0)
        # Add the node to the closed list
        closedNodes.append(node)

        # Generate all successors
        for successor in node.value.getSuccessors():
            child = astarNode(successor, parent=node)
            # Calculate heuristic, cost and f
            child.h = funcHeuristic(value=child.value, node=child)
            child.g = funcCost(value=child.value, node=child)
            child.f = child.g + child.h

            # Exit condition
            if child.value == goalValue:
                return root

            if not (child in openedNodes or child in closedNodes):
                # Add to opened if not already in opened or closed
                openedNodes.append(child)
            elif child in openedNodes:
                # If already in opened, and new cost is lower, update
                openedNode = openedNodes[openedNodes.index(child)]
                if child.g < openedNode.g:
                    openedNodes.remove(openedNode)
                    openedNodes.append(child)
            elif child in closedNodes:
                # If closed, reopen it
                closedNodes.remove(child)
                openedNodes.append(child)

        # Sort by f
        openedNodes.sort(key=lambda x: x.f)

    raise AstarException("Error: A* couldn't find a path")
