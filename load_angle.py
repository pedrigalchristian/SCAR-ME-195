import json
from dump_angle import msg

robot = json.loads(msg)

print(robot)
print(type(robot))

print(robot['joint'][0])

