from enum import (IntEnum, auto)

#region RoboRio Constants
# included to help with communication and readability
class Rio_DIO(IntEnum):
    ZERRO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    # TODO figure out how CAN works..
    TEN = auto()
    ELEVEN = auto()
    TWELVE = auto()
    THIRTEEN = auto()
    FOURTEEN = auto()
    FIFTEEN = auto()
    SIXTEEN = auto()
    SEVENTEEN = auto()

class Rio_Pnue(IntEnum):
    ZERRO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()


class Rio_PWM(IntEnum):
    ONE = 0
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()

class Rio_Relay(IntEnum):
    ZERO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()

class Rio_Analog(IntEnum):
    ZERO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
#endregion

#region CAN Constants
class CAN_Address(IntEnum):
    ZERRO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    ELEVEN = auto()
    TWELVE = auto()

#endregion
class kDrive:
    left_motor_1_port = CAN_Address.THREE
    left_motor_2_port = CAN_Address.FOUR
    right_motor_1_port = CAN_Address.ONE
    right_motor_2_port = CAN_Address.TWO

    FrontLeftEncoderPorts = (Rio_DIO.TEN, Rio_DIO.ELEVEN)
    FrontRightEncoderPorts = (Rio_DIO.TWELVE, Rio_DIO.THIRTEEN)
    BackLeftEncoderPorts = (Rio_DIO.FOURTEEN, Rio_DIO.FIFTEEN)
    BackRightEncoderPorts = (Rio_DIO.SIXTEEN, Rio_DIO.SEVENTEEN)
    
    encoder_distance_per_port = 1
    max_output = .45
    deadband = .3
    wheel_base = 1.111 # meters
    track_width = 1.112 # meters

class kOI:
    joystick_0 = 0
    joystick_1 = 1


class kTurret:
    rotation_motor = CAN_Address.ELEVEN 
    angle_motor = CAN_Address.TWELVE
    
    rotation_speed = .10
    angle_speed = .30
    
class kCannon:
    compressor_address = CAN_Address.FIVE #TODO: figure out what this should be
    relay_address = Rio_Relay.ZERO #TODO: figure out what this should be



    