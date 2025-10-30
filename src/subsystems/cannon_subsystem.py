import wpilib
from wpilib import (SmartDashboard, Compressor, Relay, PneumaticsModuleType ,)

import commands2

from constants import kCannon

class Cannon(commands2.Subsystem):
    def __init__(self) -> None:
        
        self.cannonRelay = Relay(
            kCannon.relay_address, 
            wpilib._wpilib.Relay.Direction.kBothDirections
        )
        
        self.change_relay(Relay.Value.kOff)

        # This might be useful
        '''
        self.compressor = Compressor(module=kCannon.compressor_address,
                                        moduleType=PneumaticsModuleType.CTREPCM )
        # self.compressor.enableAnalog(65,75) # (105,115)
        # self.compressor.setClosedLoopControl(True)
        '''

    def rest(self) -> None:
        self.change_relay(Relay.Value.kOff)
    
    def fire(self):
        self.change_relay(Relay.Value.kForward)
    
    def reverse(self):
        self.change_relay(Relay.Value.kReverse)
    
    def change_relay(self, value : Relay.Value):
        self.cannonRelay.set(value)
        match value:
            case Relay.Value.kForward: 
                SmartDashboard.putString("Cannon Relay State", "kForward")
            case Relay.Value.kOff: 
                SmartDashboard.putString("Cannon Relay State", "kOff")
            case Relay.Value.kOn: 
                SmartDashboard.putString("Cannon Relay State", "kOn")
            case Relay.Value.kReverse: 
                SmartDashboard.putString("Cannon Relay State", "kReverse")
