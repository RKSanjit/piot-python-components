# Constrained Device Application (Connected Devices)

## Lab Module 04


### Description


What does your implementation do? 

Implementation for Module 4 adds emulation capabilities to the Constrained Device Application (CDA) 
using the Sense HAT emulator. It allows generating simulated sensor data and handling basic actuation 
events using the emulator's LED matrix. This provides a way to test the CDA functionality before 
deploying to real devices.

How does your implementation work?

The emulator integration works by creating new sensor and actuator tasks that inherit from the base simulator 
classes in Module 3. The new emulator tasks interface with the Sense HAT emulator using the pisense Python module. 
Minor changes to the SensorAdapterManager and ActuatorAdapterManager classes were needed to initialize the 
appropriate tasks based on a configuration flag. The tasks can then generate sensor data from the emulator GUI 
controls and display actuation messages on the LED matrix. The modular design allowed adding this new functionality 
with minimal code changes.


### Code Repository and Branch

NOTE: Be sure to include the branch (e.g. https://github.com/programming-the-iot/python-components/tree/alpha001).

URL: 

### UML Design Diagram(s)

![mod3 (2)](https://github.com/RKSanjit/piot-python-components/assets/144634185/203fcb21-3d61-46cd-8b2b-6c86de8167db)



### Integration Tests Executed


- SenseHatEmulatorQuickTest.py
- HumidityEmulatorTaskTest.py
- PressureEmulatorTaskTest.py
- TemperatureEmulatorTaskTest.py
- HumidifierEmulatorTaskTest.py
- HvacEmulatorTaskTest.py
- LedDisplayEmulatorTaskTest.py
- SensorEmulatorManagerTest.py
- ActuatorEmulatorManagerTest.py.

EOF.
