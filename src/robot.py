#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
from wpilib import SmartDashboard, Field2d

from robotcontainer import RobotContainer

class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        self.container = RobotContainer()
        self.field = Field2d()
        
        SmartDashboard.putData("Field", self.field)  # Gets viewed in Glass
        SmartDashboard.putData(commands2.CommandScheduler.getInstance())

    def robotPeriodic(self):
        commands2.CommandScheduler.getInstance().run()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        pass

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        pass

    def testInit(self):
        """This function is called once each time the robot enters test mode."""
        commands2.CommandScheduler.getInstance().cancelAll()

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        pass
