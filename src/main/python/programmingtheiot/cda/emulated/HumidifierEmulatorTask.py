#####
# This class is part of the Programming the Internet of Things project.
#
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises.
# Students are encouraged to modify this class to implement a Humidifier actuator
# for an IoT system. This class simulates a Humidifier actuator and is designed for
# educational purposes. It can be customized by students to emulate Humidifier behavior
# in an IoT environment.
#

import logging
from time import sleep
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask
from pisense import SenseHAT

# Define the HumidifierEmulatorTask class, which simulates a humidifier actuator
class HumidifierEmulatorTask(BaseActuatorSimTask):
    """
    This class simulates an Humidifier actuator.
    
    """

    # Constructor: Initialize the humidifier actuator with a name, type ID, and simple name
    def __init__(self):
        super( \
            HumidifierEmulatorTask, self).__init__( \
                name = ConfigConst.HUMIDIFIER_ACTUATOR_NAME, \
                typeID = ConfigConst.HUMIDIFIER_ACTUATOR_TYPE, \
                simpleName = "HUMIDIFIER")
        
        # Get the emulator enable flag from the configuration
        enableEmulation = ConfigUtil().getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)
        
        # Initialize the SenseHAT with emulation enabled or disabled based on the configuration
        self.sh = SenseHAT(emulate = enableEmulation)


    # Method to activate the humidifier actuator
    def _activateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
    	
        # Check if a SenseHAT LED screen instance is available
        if self.sh.screen:
            msg = self.getSimpleName() + ' ON: ' + str(val) + '%'
            self.sh.screen.scroll_text(msg)
            return 0  # Success
           
        else:
            # Log a warning if there is no SenseHAT LED screen instance
            logging.warning("No SenseHAT LED screen instance to write.")
            return -1  # Failure

    # Method to deactivate the humidifier actuator
    def _deactivateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
        # Check if a SenseHAT LED screen instance is available
        
        if self.sh.screen:
            msg = self.getSimpleName() + ' OFF'
            self.sh.screen.scroll_text(msg)
            
            # Optional sleep (5 seconds) for the message to scroll before clearing the display
            sleep(5)
            
            self.sh.screen.clear()
            return 0  # Success
        else:
            # Log a warning if there is no SenseHAT LED screen instance
            logging.warning("No SenseHAT LED screen instance to clear / close.")
            return -1  # Failure
