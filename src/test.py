from arm import *
from cube import *


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
    arm.draw()
    arm.hold(A)
    print(arm)
    arm.draw()
    try:
        arm.hold(B)
    except ArmException as e:
        print(e)
    print(arm)
    arm.draw()
    arm._holding.draw()
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
    B.draw()
    A.draw()

    print("======================= END TESTS FOR CUBES =======================\n")
