so ben

the turret command and subsystem mysteriously dissapeared
go code it back

make it so it can move left/right and up/down

also the code in the code_revamp repository doesn't have the up and down so you actually have to do something original


...

you should do:
- four button binded commands that move it individually (instead of one default command that moves it with joystick)
  - you can use the plus shaped buttons on the left of the controller (povUp, povDown, povLeft, povRight)
- use robotcontainer to bind the buttons (like the fire cannon command button)
- and make the turret subsystem that uses motors that you might have to copy from the reference


...

use the code_revamp repository if you need help

ask chase or someone for more help

ooh but tell chase to teach aj basics if she's there

...


oh yeah and quick robot simulation lesson:
- when you type robotpy sim it makes a big blue window and you gotta set up a few things:
  - set "Robot State" (top left corner) to teleoperated instead of disconnected
  - drag System Joystick 0 (that you need connected) to the "0" option in the "Joysticks" window
- you can see SmartDashboard variables somehwere in the NetworkTables window
  - example of putting a number in SmartDashboard:
    - "from wpilib import SmartDashboard"
    - "SmartDashboard.putNumber("speed", 1.67)


...


push the repository to this branch when you're done

if you actually do this than you know how a subsystem works yay

good luck :)
