import logging
import unittest

from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.cda.app.DeviceDataManager import DeviceDataManager
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.DataUtil import DataUtil

class DeviceDataManagerCallbackTest(unittest.TestCase):
    """
    This test case class contains basic integration tests for DeviceDataManager, focusing on the
    callback functionality related to actuator data handling.
    """

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Testing DeviceDataManager Callback functionality...")

    def setUp(self):
     #   self.ddMgr = DeviceDataManager(enableMqtt=False, enableCoap=False)
	    pass
    def tearDown(self):
        pass

    def testActuatorDataCallback(self):
        actuatorData = ActuatorData(actuatorType=ConfigConst.HVAC_ACTUATOR_TYPE)
        actuatorData.setCommand(ConfigConst.COMMAND_ON)
        actuatorData.setStateData("This is a test.")
        actuatorData.setValue(52)

        self.ddMgr.handleActuatorCommandMessage(actuatorData)

        # Additional logging to confirm actuator data handling
        logging.info(f"Actuator Data Sent: {DataUtil.actuatorDataToJson(actuatorData)}")

        sleep(10)

if __name__ == "__main__":
    unittest.main()
