from time import sleep
from grSimPy.grSimRobot import grSimRobot


robot = grSimRobot(robot_id=0, yellow_team=True)
robot.set_velocity(0,0,0)
for i in range(10):
    robot.set_velocity((i%2)*(-2)+1,0,0)
    sleep(1)
robot.set_velocity(0,0,0)
