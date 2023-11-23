# Import necessary modules and classes
import logging
import unittest
from time import sleep
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.DefaultDataMessageListener import DefaultDataMessageListener
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.cda.connection.CoapClientConnector import CoapClientConnector
from programmingtheiot.data.DataUtil import DataUtil
from programmingtheiot.data.SensorData import SensorData

class CoapClientConnectorTest(unittest.TestCase):
    """
    This test case class contains very basic integration tests for
    CoapClientConnector using a separately running CoAP server.
    It should not be considered complete,
    but serve as a starting point for the student implementing
    additional functionality within their Programming the IoT
    environment.
    NOTE: This is different from CoapServerAdapterTest in that it depends
    upon an external CoAP server (e.g., the GDA's CoAP server).
    """

    @classmethod
    def setUpClass(self):
        # Set up logging configuration
        logging.basicConfig(format='% (asctime)s:% (module)s:% (levelname)s:% (message)s', level=logging.INFO)
        logging.info("Testing CoapClientConnector class...")

        # Create instances for necessary classes and get configuration values
        self.dataMsgListener = DefaultDataMessageListener()
        self.pollRate = ConfigUtil().getInteger(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.POLL_CYCLES_KEY, ConfigConst.DEFAULT_POLL_CYCLES)
        self.coapClient = CoapClientConnector()

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #@unittest.skip("Ignore for now.")
    def testConnectAndDiscover(self):
        """
       	Sends a discovery request and sleep for 5 seconds
        """
        
        self.coapClient.sendDiscoveryRequest(timeout=5)
        sleep(5)

    #@unittest.skip("Ignore for now.")
    def testGetActuatorCommandCon(self):
        """
        
        Send a CON GET request for the actuator command
        
        """
        self.coapClient.sendGetRequest(resource=ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE, enableCON=True, timeout=5)

    #@unittest.skip("Ignore for now.")
    def testGetActuatorCommandNon(self):
        """
     Send a CON GET request for the actuator command without using CON
     
     """
        self.coapClient.sendGetRequest(resource=ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE, enableCON=False, timeout=5)

    #@unittest.skip("Ignore for now.")
    def testDeleteSensorMessageCon(self):
        """
        Sends a CON DELETE request for the sensor message
        """
        
        self.coapClient.sendDeleteRequest(resource=ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, enableCON=True, timeout=5)

    #@unittest.skip("Ignore for now.")
    def testDeleteSensorMessageNon(self):
        """
        Sends a NON DELETE request for the sensor message
        """
        
        self.coapClient.sendDeleteRequest(resource=ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, enableCON=False, timeout=5)

    #@unittest.skip("Ignore for now.")
    def testPostSensorMessageCon(self):
        """
        Creates sensor data, convert to JSON, and send a CON POST request
        """
        
        data = SensorData()
        jsonData = DataUtil().sensorDataToJson(data=data)
        self.coapClient.sendPostRequest(resource=ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, enableCON=True, payload=jsonData, timeout=5)

    #@unittest.skip("Ignore for now.")
    def testPostSensorMessageNon(self):
        """
        Create sensor data, convert to JSON, and send a NON POST request
        """
        
        data = SensorData()
        jsonData = DataUtil().sensorDataToJson(data=data)
        self.coapClient.sendPostRequest(resource=ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, enableCON=False, payload=jsonData, timeout=5)

    #@unittest.skip("Ignore for now.")
    def testPutSensorMessageCon(self):
        """
        Creates sensor data, convert to JSON, and send a CON PUT request
        """
       
        data = SensorData()
        jsonData = DataUtil().sensorDataToJson(data=data)
        self.coapClient.sendPutRequest(resource=ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, enableCON=True, payload=jsonData, timeout=5)

    #@unittest.skip("Ignore for now.")
    def testPutSensorMessageNon(self):
        """
        Create sensor data, convert to JSON, and send a NON PUT request
        """
        
        data = SensorData()
        jsonData = DataUtil().sensorDataToJson(data=data)
        self.coapClient.sendPutRequest(resource=ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, enableCON=False, payload=jsonData, timeout=5)

    #@unittest.skip("Ignore for now.")
    def testActuatorCommandObserve(self):
        """
        Starts and stops observing actuator commands after a delay
        """
        
        self._startObserver()
        sleep(30)
        self._stopObserver()

    def _startObserver(self):
        # Start observing the actuator command resource
        self.coapClient.startObserver(resource=ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE)

    def _stopObserver(self):
        # Stop observing the actuator command resource
        self.coapClient.stopObserver(resource=ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE)

if __name__ == "__main__":
    unittest.main()
