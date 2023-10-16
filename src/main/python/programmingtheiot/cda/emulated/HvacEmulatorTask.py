import logging
from time import sleep
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask
from pisense import SenseHAT

# Define the HvacEmulatorTask class, which simulates an HVAC actuator
class HvacEmulatorTask(BaseActuatorSimTask):
    """
    This class simulates an HVAC (Heating, Ventilation, and Air Conditioning) actuator.
    """

    # Constructor: Initialize the HVAC actuator with a name, type ID, and simple name
    def __init__(self):
        super( \
            HvacEmulatorTask, self).__init__( \
                name = ConfigConst.HVAC_ACTUATOR_NAME, \
                typeID = ConfigConst.HVAC_ACTUATOR_TYPE, \
                simpleName = "HVAC")

        # Get the emulator enable flag from the configuration
        enableEmulation = ConfigUtil().getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)

        # Initialize the SenseHAT with emulation enabled or disabled based on the configuration
        self.sh = SenseHAT(emulate = enableEmulation)

    # Method to activate the HVAC actuator
    def _activateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
        # Check if a SenseHAT LED screen instance is available
        if self.sh.screen:
            msg = self.getSimpleName() + ' ON: ' + str(val) + 'C'
            self.sh.screen.scroll_text(msg)
            return 0  # Success
        else:
            # Log a warning if there is no SenseHAT LED screen instance
            logging.warning("No SenseHAT LED screen instance to write.")
            return -1  # Failure

    # Method to deactivate the HVAC actuator
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
