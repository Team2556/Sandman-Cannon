from commands2 import Subsystem
from constants import TurretConstant
import wpilib
import phoenix5

class Turret(Subsystem):
    def __init__(self):
        super().__init__()

        self.rotate_motor = phoenix5.WPI_TalonSRX(TurretConstant.kRotateMotor)
        self.rotate_motor.setNeutralMode(wpilib.NeutralMode.Brake)
        
        self.lift_motor = phoenix5.WPI_TalonSRX(TurretConstant.kLiftMotor)
        self.lift_motor.setNeutralMode(wpilib.NeutralMode.Brake)

    def move_rotate(self, speed: float):
        self.rotate_motor.set(speed)

    def move_lift(self, speed: float):
        self.lift_motor.set(speed)

    def stop_rotate(self):
        self.rotate_motor.set(0)

    def stop_lift(self):
        self.lift_motor.set(0)

    def periodic(self):
        pass
