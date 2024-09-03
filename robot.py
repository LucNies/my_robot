#from inputs import get_gamepad
import RPi.GPIO as GPIO
import Slush
import math
import time


#setCurrent(run,accel, deccel, hold) - value between 0 and 200
ELBOW_R_CURRENT = (50,50,50,50)
ELBOW_R_MAX_SPEED = 50
SHOULDER_P_CURRENT = (65, 20, 20, 65)
SHOULDER_P_MAX_SPEED = 50
SHOULDER_R_CURRENT = (65, 65, 65, 65)
SHOULDER_R_MAX_SPEED = 200



class Robot:

    def __init__(self):
        self.wrist_r = self.init_joint(0)
        self.wrist_y = self.init_joint(1)
        self.elbow_r = self.init_joint(2, ELBOW_R_MAX_SPEED, ELBOW_R_CURRENT)
        self.elbow_p = self.init_joint(3)
        self.shoulder_p0 = self.init_joint(4, SHOULDER_P_MAX_SPEED, SHOULDER_P_CURRENT)
        self.shoulder_p1 = self.init_joint(5, SHOULDER_P_MAX_SPEED, SHOULDER_P_CURRENT)
        self.shoulder_r = self.init_joint(6, SHOULDER_R_MAX_SPEED, SHOULDER_R_CURRENT)

    def init_joint(self, motor_nr, max_speed=100, current=(75,75,75,75)):
        m = Slush.Motor(motor_nr)
        m.setMaxSpeed(max_speed)
        m.setCurrent(*current)
        return m

    def move_single_joint(j, steps):
        j.move(steps)
        while j.isBusy():
            continue

    def move_shoulder_p(self, steps):
            self.shoulder_p0.move(steps)
            self.shoulder_p1.move(steps)
            while self.shoulder_p0.isBusy() and self.shoulder_p1.isBusy():
                continue

 
    def test_shoulder_r(self):
        self.move_single_joint(self.shoulder_r(100))


if __name__ == "__main__":

    robot = Robot()
    # Test joints
    robot.move_single_joint(robot.wrist_r, 100)
    robot.move_single_joint(robot.wrist_y, 100)
    robot.move_single_joint(robot.wrist_r, 100)
    robot.move_single_joint(robot.elbow_r, 100)
    robot.move_single_joint(robot.elbow_r, 100)
    robot.move_single_joint(robot.shoulder_r, 100)
    robot.move_shoulder_p(100)
    

    


    
    
