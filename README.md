# Constrained Device Application (Connected Devices)

## Lab Module 02

### Description

This implementation enables a constrained device application, ConstrainedDeviceApp, to continuously monitor system performance metrics, including CPU and memory utilization. It achieves this through scheduled polling using utility tasks, SystemCpuUtilTask and SystemMemUtilTask, which inherit from a common base task, BaseSystemUtilTask. Configuration settings are accessed via the ConfigUtil singleton. SystemPerformanceManager serves as the central orchestrator, scheduling metric retrieval and logging via the scheduler. ConstrainedDeviceApp manages the system's lifecycle, ensuring smooth operation. In essence, it establishes a structured framework for efficient system performance monitoring.

#### What does your implementation do? 

- The implementation enables a constrained device application (ConstrainedDeviceApp) to monitor system performance metrics like CPU and memory utilization
- It uses a scheduler (BackgroundScheduler) to periodically poll the metrics at a configurable interval
- The metrics are retrieved by utility tasks (SystemCpuUtilTask, SystemMemUtilTask) that extend a base task
- The metrics are logged via the handleTelemetry() method of SystemPerformanceManager
- ConstrainedDeviceApp starts and stops SystemPerformanceManager when the app starts/stops

#### How does your implementation work?

- SystemPerformanceManager is initialized with a polling interval and config settings
- When started, it schedules handleTelemetry() to run periodically via the scheduler
- handleTelemetry() gets CPU and mem utilization using the utility tasks
- Utility tasks extend BaseSystemUtilTask to implement getTelemetryValue()
- ConfigUtil provides access to config settings as a singleton
- ConstrainedDeviceApp creates SystemPerformanceManager and calls its start/stop methods

### Code Repository and Branch

URL: https://github.com/RKSanjit/piot-python-components/tree/labmodule02

### UML Design Diagram(s)


### Unit Tests Executed

- ConfigUtilTest.
- testGetTelemetryValue()

### Integration Tests Executed

- ConstrainedDeviceAppTest.
- SystemPerformanceManagerTest
