from commands2 import Subsystem
from constants import kTurret
import wpilib
import phoenix5
import phoenix6

from wpilib import SmartDashboard
class Turret(Subsystem):
    def __init__(self):
        super().__init__()

        self.track_rotation_motor = phoenix5.WPI_TalonSRX(kTurret.rotation_motor)
        # self.turret_elevation_motor = phoenix5.WPI_TalonSRX(kTurret.lift_motor)

        # SmartDashboard.putData("Turret Rotate Motor", self.turret_rotation_motor)
        # SmartDashboard.putData("Turret Lift Motor", self.turret_elevation_motor)

    def rotate_track(self, speed: float):
        SmartDashboard.putNumber("Turret Rotate Speed", speed)
        self.track_rotation_motor.set(speed)

    def disable_rotation_motor(self):
        self.rotate_track(0)

    # def elevate_turret(self, speed: float):
        # self.turret_elevation_motor.set(speed)

    # def disable_elevation_motor(self):
    #     self.elevate_turret(0)
