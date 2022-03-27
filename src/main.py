# from cube import *
# from arm import *
import test
from table import *
from astar import astar

# ====== TESTS ======
# test.testArm()
# test.testCube()
# test.testAstarNode()
# ====== END TESTS ======

# ======================== MAIN ========================


def h1(value, node=None):
    """Heuristic 1 for A* : h(x) = 6 - (ON(A,B) + ON(B,C) + ONTABLE(C))"""
    res = 6
    if (value.A.onCube(value.B)):
        res -= 1
    else:
        res += 1

    if (value.B.onCube(value.C)):
        res -= 2
    else:
        res += 2

    if (value.C.onTable()):
        res -= 3
    else:
        res += 3

    return res


def g1(value, node=None):
    return node.depth if node != None else 0


def h2(value, node):
    # TODO: implement
    return -1


def g2(value, node):
    return node.depth if node != None else 0


tableStart = Table.getTableSubjectStart()
print("tableStart:", tableStart,
      ", h1=" + str(h1(tableStart)), ", g1=" + str(g1(tableStart)))
# tableStart.draw()

tableGoal = Table.getTableSubjectGoal()
print("tableGoal:", tableGoal,
      ", h1=" + str(h1(tableGoal)), ", g1=" + str(g1(tableGoal)))
# tableGoal.draw()


tree1 = astar(h1, g1,
              Table.getTableSubjectStart(), Table.getTableSubjectGoal())
tree1.draw(dot=True, dotFileName="tree1.png")

# tree2 = astar(h2, g2,
#               Table.getTableSubjectStart(), Table.getTableSubjectGoal())
# ======================== END MAIN ========================
