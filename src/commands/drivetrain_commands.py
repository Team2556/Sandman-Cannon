import commands2
from subsystems import drivetrain_subsystem
from constants import kDrive

class DriveWithJoystick(commands2.Command):
    def __init__(
        self, drivetrain : drivetrain_subsystem.DriveTrain, 
        joystick_0 : commands2.button.CommandXboxController
    ) -> None:
        
        self.drivetrain = drivetrain
        
        self.joystick_0 = joystick_0
        
        self.addRequirements(self.drivetrain)
    
    def execute(self):
        x = self.joystick_0.getLeftY()
        z = self.joystick_0.getLeftX()
        
        self.drivetrain.arcade_drive(x, z)