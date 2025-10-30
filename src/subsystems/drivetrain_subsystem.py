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

        # Ensures POS Voltages correspond to forward for all motors
        self.FL_motor.setInverted(True)
        self.BL_motor.setInverted(True)

        self.BL_motor.follow(self.FL_motor)
        self.BR_motor.follow(self.FR_motor)
        
        self.robot_drive : wpilib.drive.DifferentialDrive = wpilib.drive.DifferentialDrive(
            self.FL_motor, 
            self.FR_motor
        )
        
        self.robot_drive.setMaxOutput(kDrive.max_output)
        self.robot_drive.setDeadband(kDrive.deadband) 
        
        # Temporary access joystick
        self.joystick_0 = commands2.button.CommandXboxController(
            kOI.joystick_0
        )

    def periodic(self) -> None:
        """This method will be called once per scheduler run"""
    
    def arcade_drive(self, x, z):
        # Using manual deadband and input modifying
        self.robot_drive.arcadeDrive(x, z, squareInputs=True)
        
        SmartDashboard.putNumber("Left Drive Motor Speeds", self.FL_motor.get() * -1)
        SmartDashboard.putNumber("Right Drive Motor Speeds", self.FR_motor.get() * -1)

