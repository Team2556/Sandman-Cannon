from commands2 import Subsystem
from constants import kTurret
import wpilib
import phoenix5
import phoenix6

from wpilib import SmartDashboard
class Turret(Subsystem):
    ...
    # WHERE DID THE CODE GO ???
    # also the "..." makes it so the class wont have an error if you put nothing after it
    def turretMobility(dpad_direction):
            print(dpad_direction)