import wpimath
import wpilib
from wpimath.geometry import Translation2d, Rotation2d

import commands2
from commands2 import CommandScheduler

from subsystems import cannon_subsystem, drivetrain_subsystem, turret_subsystem
from constants import *

class RobotContainer:
    def __init__(self):
        CommandScheduler.getInstance().run()
        self.timer = wpilib.Timer()

        self.joystick_0 = commands2.button.CommandXboxController(
            kOI.joystick_0
        )
        
        self.drive_train = drivetrain_subsystem.DriveTrain()
        self.cannon = cannon_subsystem.Cannon()
        self.turret = turret_subsystem.Turret()
    
        self.configure_default_commands()
        self.configure_button_bindings()
    
    def configure_default_commands(self):
        self.drive_train.setDefaultCommand(
            commands2.cmd.run(
                lambda: self.drive_train.driveWithJoystick(self.joystick_0),
                self.drive_train,
            )
        )
        self.cannon.setDefaultCommand(
            commands2.cmd.run(lambda: self.cannon.stop(), self.cannon)
        )
        self.turret.setDefaultCommand(
            commands2.cmd.run(lambda: self.turret.stop_rotate(), self.turret)
        )
        
    def configure_button_bindings(self):
        fire_cannon = commands2.cmd.run(lambda: self.cannon.fire()).raceWith(
            commands2.WaitCommand(0.2)
        )

        rotate_right = commands2.cmd.run(
            lambda: self.turret.move_rotate(kTurret.rotation_speed),
            self.turret,
        )
        rotate_left = commands2.cmd.run(
            lambda: self.turret.move_rotate(-kTurret.rotation_speed),
            self.turret,
        )

        # self.driverController.rightBumper().onTrue(fire_cannon)
        self.joystick_0.leftTrigger().whileTrue(rotate_left)
        self.joystick_0.rightTrigger().whileTrue(rotate_right)

        # end section
