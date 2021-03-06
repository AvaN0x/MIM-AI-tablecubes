from arm import *
from cube import *
from astar import astarNode


def testArm():
    A = Cube("A")
    B = Cube("B")

    print("======================= TESTS FOR ARM =======================")
    arm = Arm()
    print(arm)
    print("Arm is holding : " + str(arm.isHolding()))
    try:
        arm.hold(None)
    except ArmException as e:
        print(e)
    print(arm)
    arm.hold(A)
    print(arm)
    try:
        arm.hold(B)
    except ArmException as e:
        print(e)
    print(arm)
    print("======================= END TESTS FOR ARM =======================\n")


def testCube():
    print("======================= TESTS FOR CUBES =======================")
    A = Cube("A")
    print(A)
    B = Cube("B")
    print(B)
    print("Put B on A")
    B.on = A
    print(A)
    print(B)

    print("======================= END TESTS FOR CUBES =======================\n")


def testAstarNode():
    print("======================= TESTS FOR ASTAR NODES =======================")
    # These test uses Cubes only for test purposes
    node = astarNode(Cube("A"), [
        astarNode(Cube("B"), [
            astarNode(Cube("D")),
            astarNode(Cube("E"))
        ]),
        astarNode(Cube("C"), [
            astarNode(Cube("F")),
            astarNode(Cube("G"))
        ])
    ])
    node.draw(dot=True, dotFileName="test.png")
    print("======================= END TESTS FOR ASTAR NODES =======================\n")


if __name__ == "__main__":
    # testArm()
    # testCube()
    testAstarNode()
