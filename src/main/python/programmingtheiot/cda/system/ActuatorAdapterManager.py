#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from importlib import import_module

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.data.ActuatorData import ActuatorData

from programmingtheiot.cda.sim.HvacActuatorSimTask import HvacActuatorSimTask
from programmingtheiot.cda.sim.HumidifierActuatorSimTask import HumidifierActuatorSimTask

class ActuatorAdapterManager(object):
	"""
	This class manages the actuation of devices based on received commands.
	It initializes and updates environmental actuator tasks and processes actuation commands.
	"""

	
	def __init__(self, dataMsgListener: IDataMessageListener = None):

		"""
		Initializes the ActuatorAdapterManager.

		Args:
			dataMsgListener (IDataMessageListener): The data message listener for receiving actuation commands.
		"""
		
		self.dataMsgListener = dataMsgListener
	
		self.configUtil = ConfigUtil()
	
		self.useSimulator = \
			self.configUtil.getBoolean( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.ENABLE_SIMULATOR_KEY)
		self.useEmulator  = \
			self.configUtil.getBoolean( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.ENABLE_EMULATOR_KEY)
		self.deviceID     = \
			self.configUtil.getProperty( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.DEVICE_LOCATION_ID_KEY, defaultVal = ConfigConst.NOT_SET)
		self.locationID   = \
			self.configUtil.getProperty( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.DEVICE_LOCATION_ID_KEY, defaultVal = ConfigConst.NOT_SET)
	
		self.humidifierActuator = None
		self.hvacActuator       = None
		self.ledDisplayActuator = None
	
	
		self._initEnvironmentalActuationTasks()
		pass
	
	def _initEnvironmentalActuationTasks(self):

		"""
		Initializes environmental actuation tasks based on configuration.
		"""
		
		if not self.useEmulator:
		# load the environmental tasks for simulated actuation
			self.humidifierActuator = HumidifierActuatorSimTask()
		
		# create the HVAC actuator
			self.hvacActuator = HvacActuatorSimTask()
	
	def sendActuatorCommand(self, data: ActuatorData) -> bool:
		
		"""
		Sends an actuation command and processes the response.

		Args:
			data (ActuatorData): The actuation command data to be processed.

		Returns:
			bool: True if the actuation command was processed successfully, else False.
		"""
		
		if data and not data.isResponseFlagEnabled():
		# first check if the actuation event is destined for this device
			if data.getLocationID() == self.locationID:
				logging.info("Actuator command received for location ID %s. Processing...", str(data.getLocationID()))
			
				aType = data.getTypeID()
				responseData = None
			
			# TODO: implement appropriate logging and error handling
				if aType == ConfigConst.HUMIDIFIER_ACTUATOR_TYPE and self.humidifierActuator:
					responseData = self.humidifierActuator.updateActuator(data)
				elif aType == ConfigConst.HVAC_ACTUATOR_TYPE and self.hvacActuator:
					responseData = self.hvacActuator.updateActuator(data)
				elif aType == ConfigConst.LED_DISPLAY_ACTUATOR_TYPE and self.ledDisplayActuator:
					responseData = self.ledDisplayActuator.updateActuator(data)
				else:
					logging.warning("No valid actuator type. Ignoring actuation for type: %s", data.getTypeID())
				
				return responseData
			else:
				logging.warning("Location ID doesn't match. Ignoring actuation: (me) %s != (you) %s", str(self.locationID), str(data.getLocationID()))
		else:
			logging.warning("Actuator request received. Message is empty or response. Ignoring.")
	
		return None
		pass
	
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		"""
		Sets the data message listener for receiving actuation commands.

		Args:
			listener (IDataMessageListener): The data message listener to be set.

		Returns:
			bool: True if the data message listener was set successfully, else False.
		"""
		if listener:
			self.dataMsgListener = listener
		pass
