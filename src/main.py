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


def h1(table):
    res = 6
    if (table.A.onCube(table.B)):
        res += 1
    else:
        res -= 1

    if (table.B.onCube(table.C)):
        res += 2
    else:
        res -= 2

    if (table.C.free):
        res += 3
    else:
        res -= 3

    return res


def g1(table):
    # TODO: implement
    pass


def h2(table):
    # TODO: implement
    pass


def g2(table):
    # TODO: implement
    pass


tableStart = Table.getTableSubjectStart()
print(tableStart)
tableStart.draw()
tableGoal = Table.getTableSubjectGoal()
print(tableGoal)
tableGoal.draw()

# tree1 = astar(h1, g1,
#               Table.getTableSubjectStart(), Table.getTableSubjectGoal())

# tree2 = astar(h2, g2,
#               Table.getTableSubjectStart(), Table.getTableSubjectGoal())
# ======================== END MAIN ========================
