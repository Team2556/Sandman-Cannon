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

        self.controller_0 = commands2.button.CommandXboxController(
            kOI.controller_0
        )
        


        
        self.drive_train = drivetrain_subsystem.DriveTrain()
        self.cannon = cannon_subsystem.Cannon()
        self.turret = turret_subsystem.Turret()
    
        self.configure_default_commands()
        self.configure_button_bindings()
    
    def configure_default_commands(self):
        
        self.drivetrain_command = drivetrain_commands.DriveWithJoystick(self.drive_train, self.controller_0)
        self.drive_train.setDefaultCommand(self.drivetrain_command)
        
        # Look at the whiteboard to figure out what this is vvv
        # self.turret_default_command = turret_commands.MoveTurretWithJoystick(self.turret, self.controller_0)
        # self.turret.setDefaultCommand(self.turret_default_command)
        
    def configure_button_bindings(self):
        # Estal\blshinsgfg a command
        # self.fire_cannon_command = (
        #     cannon_commands.FireCannon(self.cannon)
        #     .withInterruptBehavior(commands2.InterruptionBehavior.kCancelIncoming)
        # )
        
# Assigns the command
        self.turret_command_up = turret_commands.turretCommands(self.turret, 0)
        self.turret_command_down = turret_commands.turretCommands(self.turret, 180)
        self.turret_command_left = turret_commands.turretCommands(self.turret, 270)
        self.turret_command_right = turret_commands.turretCommands(self.turret, 90)




        self.controller_0.povUp().onTrue(self.turret_command_up)
        self.controller_0.povDown().onTrue(self.turret_command_down)
        self.controller_0.povLeft().onTrue(self.turret_command_left)
        self.controller_0.povRight().onTrue(self.turret_command_right)

