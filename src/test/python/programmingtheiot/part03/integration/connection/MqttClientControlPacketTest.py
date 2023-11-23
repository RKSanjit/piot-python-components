import logging
import unittest
 
from time import sleep
 
import programmingtheiot.common.ConfigConst as ConfigConst
 
from programmingtheiot.cda.connection.MqttClientConnector import MqttClientConnector
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.common.DefaultDataMessageListener import DefaultDataMessageListener
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData 
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData 
from programmingtheiot.data.DataUtil import DataUtil
 
class MqttClientControlPacketTest(unittest.TestCase):
    
    """
    Unit tests for testing control packet functionality in MqttClientConnector.
    This includes testing connect, disconnect, server ping, and publish/subscribe operations.
    """

    @classmethod
    def setUpClass(self):
        
        """
        Set up class method for initializing logging and MQTT Client Connector.
        Uses a different client ID than the CDA for testing purposes.
        """        

        
        logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
        logging.info("Executing the MqttClientControlPacketTest class...")
        self.cfg = ConfigUtil()
        # NOTE: Be sure to use a DIFFERENT clientID than that which is used
        # for your CDA when running separately from this test
        # 
        # The clientID shown below is an example only - please use your own
        # unique value for this test
        self.mcc = MqttClientConnector(clientID = "MyTestMqttClient")
 
    def setUp(self):
        pass
 
    def tearDown(self):
        pass
 
    def testConnectAndDisconnect(self):
        
        """
        Test the MQTT client's ability to connect and disconnect from the broker.
        """
        
        logging.info("Testing connect and disconnect...")
        self.assertTrue(self.mcc.connectClient())
        logging.info("Connected to the MQTT broker.")
        sleep(1)  # Small delay to ensure connection establishment
        self.assertTrue(self.mcc.disconnectClient())
        logging.info("Disconnected from the MQTT broker.")
 
    def testServerPing(self):
        
        """
        Test the MQTT client's ability to ping the server to keep the connection alive.
        """
        
 
        logging.info("Testing server ping...")
        self.assertTrue(self.mcc.connectClient())
        logging.info("Connected to the MQTT broker.")
        # Assuming a keep-alive interval smaller than this sleep time
        sleep(2 * self.cfg.getKeepAlive())
        # The actual PINGREQ and PINGRESP would have to be validated through logs
        logging.info("Ping should have occurred.")
        self.assertTrue(self.mcc.disconnectClient())
        logging.info("Disconnected from the MQTT broker after ping test.")
 
 
    def testPubSub(self):
        
        """
        Test publish and subscribe functionality of the MQTT client with different QoS levels.
        """
        
        
        topic = ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE
        test_message_qos1 = 'Test message QoS 1'
        test_message_qos2 = 'Test message QoS 2'
        
        logging.info("Testing publish and subscribe with QoS 1 and QoS 2...")
        
        self.assertTrue(self.mcc.connectClient())
        logging.info("Connected to the MQTT broker.")
      
        self.assertTrue(self.mcc.subscribeToTopic(topic, self.mcc.onMessage, 1))
        logging.info(f"Subscribed to {topic} with QoS 1.")
        self.assertTrue(self.mcc.publishMessage(topic, test_message_qos1, 1))
        logging.info(f"Published message with QoS 1: {test_message_qos1}")
        
        self.assertTrue(self.mcc.unsubscribeFromTopic(topic))
        logging.info(f"Unsubscribed from {topic}.")


        self.assertTrue(self.mcc.subscribeToTopic(topic, self.mcc.onMessage, 2))
        logging.info(f"Subscribed to {topic} with QoS 2.")
        self.assertTrue(self.mcc.publishMessage(topic, test_message_qos2, 2))
        logging.info(f"Published message with QoS 2: {test_message_qos2}")
        
        self.assertTrue(self.mcc.unsubscribeFromTopic(topic))
        logging.info(f"Unsubscribed from {topic}.")
        
        self.assertTrue(self.mcc.disconnectClient())
        logging.info("Disconnected from the MQTT broker after pub/sub test.")
        

if __name__ == '__main__':
    unittest.main()
    
    