# Constrained Device Application (Connected Devices)

## Lab Module 03


### Description

What does your implementation do? 

The implementation simulates and manages both sensors and actuators within a modular framework. 
At its core, the system can simulate sensing functionalities, capturing diverse data points from virtual sensors and determining
if the data demands a reactive measure, such as triggering an actuator. 
In addition to the sensor simulations, the framework also possesses the capability to simulate actuator tasks. 
Based on the data from the sensors, these actuators can perform specific actions, making the system dynamic and responsive. 
The overarching design follows three principles: measuring data from simulated sensors, modelling the components for modular integration, 
and managing the flow of data and actions within the system.

How does your implementation work?

- The handleTelemetry() function continuously polls each sensor, collecting its data, and forwards this data to the self.dataMsgListener callback. 
  This ensures the system is continually updated with the latest readings from all simulated sensors.
- The SystemPerformanceManager class possibly oversees the operations of both sensor and actuator simulators.
- The system emphasizes data validation, especially when processing actuator commands.
- Before executing any command, the system validates the ActuatorData typeID by checking it against a list of known actuator simulators.
- If a match is found, the corresponding ActuatorData instance is passed to the appropriate actuator task, ensuring only legitimate actuator commands are processed.

### Code Repository and Branch


URL: https://github.com/RKSanjit/piot-python-components/tree/labmodule03

### UML Design Diagram(s)

![mod3](https://github.com/RKSanjit/piot-python-components/assets/144634185/d9dea692-5eb9-41ef-88c7-6fa280c996dd)


### Unit Tests Executed

- ActuatorDataTest
- SensorDataTest
- SystemPerformanceDataTest
- HumiditySensorSimTaskTest
- PressureSensorSimTaskTest
- TemperatureSensorSimTaskTest
- HumidifierActuatorSimTaskTest
- HvacActuatorSimTaskTest
- BaseIotDataTest

### Integration Tests Executed

- ActuatorAdapterManagerTest
- SensorAdapterManagerTest
- DeviceDataManagerNoCommsTest.
- ConstrainedDeviceAppTest.

EOF.
