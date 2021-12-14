import pprint
import json

angle1 = 90
angle2 = 20
angle3 = -10
angle4 = 50
angle5 = 21

# 1. Global Variables / Nested Lists
# 2. OOP (Classes)
# 3. JSON

joint = [20, 21, 21, 21, 21] # List of Lists


robot = {
    # "joint" : [angle1, angle2, angle3, angle4, angle5]
    "joint" : joint
}

print(robot)



robot["lol"] = "This is a test"

print(robot["lol"])



msg = json.dumps(robot)

"""
Benefit #1: Scalable ;;; Why do we need nesting? --> Good way to organize code so ppl know which variables encompass one object
Benefit #2: Very computationally efficient way to save object-oriented variables. (e.g., ROS, DonkeyCar)
"""


