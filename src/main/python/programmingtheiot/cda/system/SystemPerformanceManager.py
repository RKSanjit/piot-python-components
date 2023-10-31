#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from apscheduler.schedulers.background import BackgroundScheduler

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.cda.system.SystemCpuUtilTask import SystemCpuUtilTask
from programmingtheiot.cda.system.SystemMemUtilTask import SystemMemUtilTask

from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData

class SystemPerformanceManager(object):
    """
    This class manages system performance data and periodically sends telemetry updates to a registered listener.
    
    Attributes:
        - pollRate: The interval (in seconds) at which system performance data is collected and sent.
        - locationID: The location ID of the constrained device.
        - dataMsgListener: The listener for receiving system performance data.
        - scheduler: A scheduler for periodically collecting and sending system performance data.
        - cpuUtilTask: An instance of the SystemCpuUtilTask for collecting CPU utilization.
        - memUtilTask: An instance of the SystemMemUtilTask for collecting memory utilization.
    """
    
    def __init__(self):
        # Initialize the configuration utility to retrieve settings
        configUtil = ConfigUtil()

        # Get the poll rate from the configuration, or use the default value if not set
        self.pollRate = configUtil.getInteger(
            section=ConfigConst.CONSTRAINED_DEVICE,
            key=ConfigConst.POLL_CYCLES_KEY,
            defaultVal=ConfigConst.DEFAULT_POLL_CYCLES
        )

        # Get the location ID from the configuration, or use the default value if not set
        self.locationID = configUtil.getProperty(
            section=ConfigConst.CONSTRAINED_DEVICE,
            key=ConfigConst.DEVICE_LOCATION_ID_KEY,
            defaultVal=ConfigConst.NOT_SET
        )

        # Ensure that the poll rate is at least the default value if it's set to 0 or less
        if self.pollRate <= 0:
            self.pollRate = ConfigConst.DEFAULT_POLL_CYCLES

        # Initialize the data message listener as None
        self.dataMsgListener = None

        # Create a scheduler and add the handleTelemetry job to run at the specified interval
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.handleTelemetry, 'interval', seconds=self.pollRate)

        # Initialize the CPU and memory utilization tasks
        self.cpuUtilTask = SystemCpuUtilTask()
        self.memUtilTask = SystemMemUtilTask()

    def handleTelemetry(self):
        """
        Collects system performance data and sends it to the registered data message listener.
        """
        # Get CPU and memory utilization values
        self.cpuUtilPct = self.cpuUtilTask.getTelemetryValue()
        self.memUtilPct = self.memUtilTask.getTelemetryValue()

        # Log the collected data
        logging.info('CPU utilization is %s percent, and memory utilization is %s percent.',
                      str(self.cpuUtilPct), str(self.memUtilPct))

        # Create a SystemPerformanceData object with the collected data
        sysPerfData = SystemPerformanceData()
        sysPerfData.setLocationID(self.locationID)
        sysPerfData.setCpuUtilization(self.cpuUtilPct)
        sysPerfData.setMemoryUtilization(self.memUtilPct)

        # If a data message listener is registered, send the data to it
        if self.dataMsgListener:
            self.dataMsgListener.handleSystemPerformanceMessage(data=sysPerfData)

    def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
        """
        Sets the data message listener for this manager.

        Args:
            listener: The data message listener to be registered.

        Returns:
            bool: True if the listener is set successfully, False otherwise.
        """
        if listener:
            self.dataMsgListener = listener
        return True

    def startManager(self):
        """
        Starts the SystemPerformanceManager and the data collection scheduler.
        """
        logging.info("Starting SystemPerformanceManager...")
        if not self.scheduler.running:
            self.scheduler.start()
            logging.info("Started SystemPerformanceManager.")
        else:
            logging.warning("SystemPerformanceManager scheduler already started. Ignoring.")

    def stopManager(self):
        """
        Stops the SystemPerformanceManager and the data collection scheduler.
        """
        logging.info("Stopped SystemPerformanceManager.")
        try:
            self.scheduler.shutdown()
            logging.info("Stopped SystemPerformanceManager.")
        except:
            logging.warning("SystemPerformanceManager scheduler already stopped. Ignoring.")
