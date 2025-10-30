import commands2
from wpilib import Timer, SmartDashboard
from subsystems import cannon_subsystem
from constants import kCannon

class FireCannon(commands2.Command):
    def __init__(self, cannon : cannon_subsystem.Cannon) -> None:
        
        self.cannon = cannon
        
        self.addRequirements(self.cannon)
        
        self.timer = Timer()
    
    def initialize(self):
        self.cannon.fire()
        self.timer.reset()
        self.timer.start()

    def execute(self):
        SmartDashboard.putNumber("Cannon Hold Time", self.timer.get())

    def isFinished(self):
        return self.timer.get() > kCannon.activate_time

    def end(self, interrupted):
        self.cannon.reverse()