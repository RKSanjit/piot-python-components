#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import random
import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask

class HvacActuatorSimTask(BaseActuatorSimTask):
	"""
	This class simulates the behavior of an HVAC (Heating, Ventilation, and Air Conditioning) actuator.
	It inherits from BaseActuatorSimTask.
	"""


	def __init__(self):

		"""
		Initializes the HVACActuatorSimTask.

		The constructor sets the name, typeID, and simpleName of the HVAC actuator.
		"""
		
		super(HvacActuatorSimTask, self).__init__(
			name=ConfigConst.HVAC_ACTUATOR_NAME,
			typeID=ConfigConst.HVAC_ACTUATOR_TYPE,
			simpleName="HVAC"
		)
		pass
		