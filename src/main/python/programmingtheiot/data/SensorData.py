#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.BaseIotData import BaseIotData

class SensorData(BaseIotData):

		
	def __init__(self, typeID: int = ConfigConst.DEFAULT_SENSOR_TYPE, name = ConfigConst.NOT_SET, d = None):
		"""
		Call the constructor of the parent class (BaseIotData)
		initialize class-scoped variables for value.
		
		@param typeID: The type ID for the sensor (default: ConfigConst.DEFAULT_SENSOR_TYPE).
		@param name: The name of the sensor (default: ConfigConst.NOT_SET).
	
		"""
		super(SensorData, self).__init__(name = name, typeID = typeID, d = d)
		
		# Initialize class-scoped variable for sensor value with a default value.
		self.value = ConfigConst.DEFAULT_VAL
		
	
	def getSensorType(self) -> int:
		"""
		@return: The sensor type as an integer
		"""
		return self.typeID
	
	def getValue(self) -> float:
		"""
		@return: The sensor value as a float
		"""
		return self.value
		
	
	def setValue(self, newVal: float):
		"""
		@param:  newVal: The new sensor value to set as a float.
		
		Update the time stamp by invoking the base class self.updateTimeStamp()
		"""
		self.value = newVal
		self.updateTimeStamp()
		
		
	def _handleUpdateData(self, data):
		"""
		Handle updating the SensorData properties from another SensorData object.

		@param: param data: The SensorData object to update from.
		"""
		
		if data and isinstance(data, SensorData):
			self.value = data.getValue()
		
	
	def __str__(self):
    		return "SensorData [name={}, typeID={}, value={}, timeStamp={}]".format(
            	self.getName(), self.getTypeID(), self.getValue(), self.getTimeStamp())
