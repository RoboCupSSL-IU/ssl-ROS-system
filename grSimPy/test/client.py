from time import sleep
from grSimPy.grSimRobot import grSimRobot, grSimVision


robot = grSimRobot(robot_id=1, yellow_team=False)
vision = grSimVision()
while(True):
    vision.receive()
    vision.get_robots()
    robot.action.set_velocity(1,1,1)
    robot.send()

    print(vision.get_position(robot_id=1, team="blue"))

robot.action.set_velocity(0,0,0)
robot.send()
for i in range(10):
    robot.action.set_velocity((i%2)*(-2)+1,0,0)
    robot.send()
    sleep(1)
robot.action.set_velocity(0,0,0)
robot.send()
