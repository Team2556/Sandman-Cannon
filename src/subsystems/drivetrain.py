from wpilib import SmartDashboard
from wpimath.geometry import Rotation2d
import wpilib
import wpilib.drive

import commands2
import phoenix5
import math

from constants import *

class DriveTrain(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.FL_motor = phoenix5.WPI_TalonSRX(kDrive.left_motor_1_port)
        self.BL_motor = phoenix5.WPI_TalonSRX(kDrive.left_motor_2_port)
        self.FR_motor = phoenix5.WPI_TalonSRX(kDrive.right_motor_1_port)
        self.BR_motor = phoenix5.WPI_TalonSRX(kDrive.right_motor_2_port)

        SmartDashboard.putData("frontLeftMotor -from drivetrain", self.FL_motor)
        SmartDashboard.putData("frontRightMotor -from drivetrain", self.FR_motor)
        SmartDashboard.putData("backLeftMotor -from drivetrain", self.BL_motor)
        SmartDashboard.putData("backRightMotor -from drivetrain", self.BR_motor)

        # Ensures POS Voltages correspond to forward for all motors
        self.FL_motor.setInverted(True)
        self.BL_motor.setInverted(True)

        self.BL_motor.follow(self.FL_motor)
        self.BR_motor.follow(self.FR_motor)
        
        self.robot_drive = wpilib.drive.DifferentialDrive(
            self.FL_motor, self.FR_motor
        )
        self.robot_drive.setMaxOutput(kDrive.max_output)
        self.robot_drive.setDeadband(kDrive.deadband) 

    def periodic(self) -> None:
        """This method will be called once per scheduler run"""
        pass

    # TODO: Setup Command File
    # def driveWithJoystick(self, joystick: wpilib.Joystick):
    #     """Drives the robot using the joystick"""
    #     self.robot_drive.arcadeDrive(
    #         -joystick.getLeftY(), -((joystick.getRightX()) ** 5)
    #     )
    
    def arcade_drive(self, x, y):
        self.robot_drive.arcadeDrive(x, y)

    def stop(self) -> None:
        self.robot_drive.driveCartesian(0, 0, 0)

