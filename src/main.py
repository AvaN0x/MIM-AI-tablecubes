import test
from table import *
from astar import astar
import utils
from colorama import Fore, Style  # pip install colorama

# ======================== MAIN ========================


def h1(value, node=None):
    """Heuristic 1 for A* : h(x) = 6 - (ON(A,B) + ON(B,C) + ONTABLE(C))"""
    res = 6
    if (value.getCube(label="A").onCube(value.getCube(label="B"))):
        res -= 1
    else:
        res += 1

    if (value.getCube(label="B").onCube(value.getCube(label="C"))):
        res -= 2
    else:
        res += 2

    if (value.getCube(label="C").onTable()):
        res -= 3
    else:
        res += 3

    return res


def g1(value, node=None):
    """Count of move executed"""
    return node.depth if node != None else 0


def h2(value, node=None):
    """Difference count between the current node and the goal"""
    res = 0

    if (not value.getCube(label="C").onTable()):
        res += 1
    if (value.getCube(label="C").free):
        res += 1
    if (not value.getCube(label="B").onCube(value.getCube(label="C"))):
        res += 1
    if (value.getCube(label="B").free):
        res += 1
    if (not value.getCube(label="A").onCube(value.getCube(label="B"))):
        res += 1
    if (not value.getCube(label="A").free):
        res += 1

    return res


def g2(value, node=None):
    """Count of move executed"""
    return node.depth if node != None else 0


print(f"{Fore.YELLOW}Table states{Style.RESET_ALL}")
tableStart = Table.getTableSubjectStart()
print(f"{Fore.CYAN}Table subject start (h1={Fore.BLUE}{h1(tableStart)}{Fore.CYAN}, g1={Fore.BLUE}{g1(tableStart)}{Fore.CYAN}, h2={Fore.BLUE}{h2(tableStart)}{Fore.CYAN}, g2={Fore.BLUE}{g2(tableStart)}{Fore.CYAN}) :{Style.RESET_ALL}")
print(str(tableStart))

tableGoal = Table.getTableSubjectGoal()
print(f"{Fore.CYAN}Table subject goal (h1={Fore.BLUE}{h1(tableGoal)}{Fore.CYAN}, g1={Fore.BLUE}{g1(tableGoal)}{Fore.CYAN}, h2={Fore.BLUE}{h2(tableGoal)}{Fore.CYAN}, g2={Fore.BLUE}{g2(tableGoal)}{Fore.CYAN}) :{Style.RESET_ALL}")
print(str(tableGoal))


print(f"{Fore.YELLOW}\nA*{Style.RESET_ALL}")
print(
    f"{Fore.CYAN}Processing A* with {Fore.BLUE}h1{Fore.CYAN} and {Fore.BLUE}g1{Fore.CYAN}...{Style.RESET_ALL}")
# tree1 = astar(h1, g1,
#               Table.getTableSubjectStart(), Table.getTableSubjectGoal())
tree1 = utils.PrintElapsedTime(func=lambda:
                               astar(h1, g1, Table.getTableSubjectStart(), Table.getTableSubjectGoal()))
tree1.draw(dot=True, dotFileName="tree1.png")

print(
    f"{Fore.CYAN}Processing A* with {Fore.BLUE}h2{Fore.CYAN} and {Fore.BLUE}g2{Fore.CYAN}...{Style.RESET_ALL}")
# tree2 = astar(h2, g2,
#               Table.getTableSubjectStart(), Table.getTableSubjectGoal())
tree2 = utils.PrintElapsedTime(func=lambda:
                               astar(h2, g2, Table.getTableSubjectStart(), Table.getTableSubjectGoal()))
tree2.draw(dot=True, dotFileName="tree2.png")
# ======================== END MAIN ========================
