import wpimath
import wpilib
from wpimath.geometry import Translation2d, Rotation2d

import commands2
from commands2 import CommandScheduler

from subsystems import cannon_subsystem, drivetrain_subsystem, turret_subsystem
from commands import cannon_commands, drivetrain_commands, turret_commands
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
        
        self.drivetrain_command = drivetrain_commands.DriveWithJoystick(self.drive_train, self.joystick_0)
        self.drive_train.setDefaultCommand(self.drivetrain_command)
        
        self.turret_default_command = turret_commands.MoveTurretWithJoystick(self.turret, self.joystick_0)
        self.turret.setDefaultCommand(self.turret_default_command)
        
        # Not looked at yet:
        # self.cannon.setDefaultCommand(
        #     commands2.cmd.run(lambda: self.cannon.stop(), self.cannon)
        # )
        
    def configure_button_bindings(self):
        
        self.fire_cannon_command = (
            cannon_commands.FireCannon(self.cannon)
            .withInterruptBehavior(commands2.InterruptionBehavior.kCancelIncoming)
        )
        self.joystick_0.b().onTrue(self.fire_cannon_command)
        
        # Not using triggers for turret movement
        # rotate_right = commands2.cmd.run(
        #     lambda: self.turret.move_rotate(kTurret.rotation_speed),
        #     self.turret,
        # )
        
        # rotate_left = commands2.cmd.run(
        #     lambda: self.turret.move_rotate(-kTurret.rotation_speed),
        #     self.turret,
        # )
