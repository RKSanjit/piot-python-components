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
from programmingtheiot.cda.system.SystemMemUtilTask import SystemMemUtilTask

class SystemPerformanceData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
	DEFAULT_VAL = 0.0
	
	def __init__(self, d = None):
		"""
		Constructor for SystemPerformanceData.

		:param d: The data dictionary (default: None).
		"""
		# Call the constructor of the parent class (BaseIotData)
		super(SystemPerformanceData, self).__init__(name = ConfigConst.SYSTEM_PERF_MSG, typeID = ConfigConst.SYSTEM_PERF_TYPE, d = d)
		
		# Initialize class-scoped variables with default values.
		self.cpuUtil = ConfigConst.DEFAULT_VAL
		self.memUtil = ConfigConst.DEFAULT_VAL
		pass
	
	def getCpuUtilization(self):
		"""
		@return: CPU Utilization as a float
		"""
		return self.cpuUtil
		pass
	
	def getDiskUtilization(self):
		
		pass
	
	def getMemoryUtilization(self):
		"""
		@return: The memory utilization as a float.
		"""
		return self.memUtil
		pass
	
	def setCpuUtilization(self, cpuUtil):
		"""
		@return: The CPU utilization value to set as a float.
		"""
		
		self.cpuUtil = cpuUtil
		self.updateTimeStamp()
		pass
	
	def setDiskUtilization(self, diskUtil):
		pass
	
	def setMemoryUtilization(self, memUtil):
		"""
		@param: The memory utilization value to set as a float.
		""" 
		self.memUtil = memUtil
		self.updateTimeStamp()
		pass
	
	def _handleUpdateData(self, data):
		"""
		@param: data: The SystemPerformanceData object to update from.
		""" 
		
		if data and isinstance(data, SystemPerformanceData):
			self.cpuUtil = data.getCpuUtilization()
			self.memUtil = data.getMemoryUtilization()
		
		pass
	
	def __str__(self):
		return "SystemPerformanceData [CPU Utilization={:.2f}%, Memory Utilization={:.2f}%]".format(
			self.cpuUtil, self.memUtil)
