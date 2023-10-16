#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.SensorData import SensorData

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask

from pisense import SenseHAT

class HumiditySensorEmulatorTask(BaseSensorSimTask):
	"""
	This task emulates a humidity sensor and generates humidity sensor data.
	
	"""

	def __init__(self):
		
		 # Call the constructor of the parent class
		super( \
			HumiditySensorEmulatorTask, self).__init__( \
				name = ConfigConst.HUMIDITY_SENSOR_NAME, \
				typeID = ConfigConst.HUMIDITY_SENSOR_TYPE)
		
		  # Read a configuration value to determine whether to enable emulation
		enableEmulation = \
			ConfigUtil().getBoolean( \
				ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)
			
		 # Initialize the SenseHAT emulator with emulate = True
		self.sh = SenseHAT(emulate = enableEmulation)
	
	def generateTelemetry(self) -> SensorData:
		
		"""
		This method is responsible for generating sensor data.
		"""
		# Create a SensorData instance for the humidity sensor
		sensorData = SensorData(name = self.getName(), typeID = self.getTypeID())
		
		# Read the humidity value from the SenseHAT emulator
		sensorVal = self.sh.environ.humidity
		
        # Set the humidity value in the SensorData object		
		sensorData.setValue(sensorVal)
		
		# Store the latest sensor data in the class variable
		self.latestSensorData = sensorData
		
		return sensorData
