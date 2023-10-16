#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

# Import necessary modules and classes
from programmingtheiot.data.SensorData import SensorData
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from pisense import SenseHAT

class TemperatureSensorEmulatorTask(BaseSensorSimTask):
    """
    This class emulates a temperature sensor and generates temperature sensor data.
    """
    
    def __init__(self):
        
        # Call the constructor of the parent class
        super( \
        TemperatureSensorEmulatorTask, self).__init__( \
            name = ConfigConst.TEMP_SENSOR_NAME, \
            typeID = ConfigConst.TEMP_SENSOR_TYPE)
        
        # Read a configuration value to determine whether to enable emulation
        enableEmulation = \
            ConfigUtil().getBoolean( \
                ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)
        
        # Initialize the SenseHAT emulator with the 'emulate' flag based on configuration
        self.sh = SenseHAT(emulate = enableEmulation)
    
    def generateTelemetry(self) -> SensorData:
        
        # Create a SensorData instance for the temperature sensor
        sensorData = SensorData(name = self.getName(), typeID = self.getTypeID())
        
        # Get the temperature value from the Sense HAT emulator
        sensorVal = self.sh.environ.temperature
        
        # Set the temperature value in the SensorData instance
        sensorData.setValue(sensorVal)
        
        # Store the latest sensor data in the class variable
        self.latestSensorData = sensorData
        
        # Return the generated sensor data
        return sensorData
