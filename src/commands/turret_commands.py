import commands2
from subsystems import turret_subsystem
from constants import kTurret

class turretCommands(commands2.Command):
    
    # WOAH YOU HAVE TO FIGURE OUT DEFAULT COMMANDS WITH THIS ONE
    def __init__(self, turret : turret_subsystem.Turret, direction) -> None:
        
        self.turret = turret
        self.direction = direction

        self.addRequirements(self.turret)

    def initialize(self):
        self.turret.turretMobility(self.direction)
        
    def execute(self):
        ...

    