import commands2
from subsystems import turret_subsystem
from constants import kTurret

class MoveTurretWithJoystick(commands2.Command):
    def __init__(self, turret : turret_subsystem.Turret, joystick : commands2.button.CommandXboxController) -> None:
        
        self.turret = turret
        self.joystick = joystick
        
        self.addRequirements(self.turret)
    
    def execute(self):
        rotate_speed = self.joystick.getRightX() ** 3 #try to allow for fine control
        # lift_speed = self.joystick.getRightY() ** 3
        self.turret.rotate_track(rotate_speed * kTurret.rotation_speed_multiplier)
        # self.turret.elevate_turret(lift_speed)

class RotateTurretConstantSpeed(commands2.Command):
    def __init__(self, turret : turret_subsystem.Turret, speed : float) -> None:
        self.turret = turret
        self.speed = speed
        
        self.addRequirements(self.turret)
    
    def execute(self):
        self.turret.rotate_track(self.speed)