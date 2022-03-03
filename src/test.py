from arm import *
from cube import *


def testArm():
    A = Cube("A")
    B = Cube("B")

    print("======================= TESTS FOR ARM =======================")
    arm = Arm()
    print(arm)
    print(str(arm.isHolding()))
    try:
        arm.hold(None)
    except ArmException as e:
        print(e)
    print(arm)
    arm.hold(A)
    print(arm)
    arm.hold(B)
    print(arm)
    print("======================= END TESTS FOR ARM =======================\n")


def testCube():
    print("======================= TESTS FOR CUBES =======================")
    A = Cube("A")
    B = Cube("B")
    print(B)
    B.on = A
    print(B)
    print("======================= END TESTS FOR CUBES =======================\n")
