#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask

from pisense import SenseHAT

class LedDisplayEmulatorTask(BaseActuatorSimTask):
	"""
	This class is intended for simulating an LED display actuator.
	
	"""
	 # Constructor: Initialize the LED display actuator with a name, type ID, and simple name
	def __init__(self):
		super( \
			LedDisplayEmulatorTask, self).__init__( \
				name = ConfigConst.LED_ACTUATOR_NAME, \
				typeID = ConfigConst.LED_DISPLAY_ACTUATOR_TYPE, \
				simpleName = "LED_Display")
		# Get the emulator enable flag from the configuration
		enableEmulation = ConfigUtil().getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)

		# Initialize the SenseHAT with emulation enabled or disabled based on the configuration
		self.sh = SenseHAT(emulate = enableEmulation)

	# Method to activate the LED display
	def _activateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
		
		# Check if a SenseHAT LED screen instance is available
		if self.sh.screen:
			
			 # Scroll the specified text on the LED screen with a font size of 8
			self.sh.screen.scroll_text(stateData, size = 8)
			
			return 0
		
		else:
			
			# Log a warning if there is no SenseHAT LED screen instance
			logging.warning("No SenseHAT LED screen instance to write.")
			
			
			return -1
	
	 # Method to deactivate the LED display
	def _deactivateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
		
		 # Check if a SenseHAT LED screen instance is available
		if self.sh.screen:
			
			# Clear the LED screen, effectively turning it off
			self.sh.screen.clear()
			
			return 0 # Success
		else:
			
			 # Log a warning if there is no SenseHAT LED screen instance
			logging.warning("No SenseHAT LED screen instance to clear / close.")
			return -1 # Failure
	