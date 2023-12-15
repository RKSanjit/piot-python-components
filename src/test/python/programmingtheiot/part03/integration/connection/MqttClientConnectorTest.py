#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
#
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
from programmingtheiot.data.DataUtil import DataUtil
class MqttClientConnectorTest(unittest.TestCase):
	"""
	This class contains unit tests for MqttClientConnector.
	It provides basic tests for MQTT connectivity and message handling
	within the Programming the IoT environment.
	"""
	@classmethod
	def setUpClass(self):
		"""
		Set up class method to initialize logging and configuration before tests.
		"""
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing MqttClientConnector class...")
		self.cfg = ConfigUtil()
		self.mcc = MqttClientConnector()
	def setUp(self):
		pass
	def tearDown(self):
		pass
	#@unittest.skip("Ignore for now.")
	def testConnectAndDisconnect(self):
		"""
		Test the MQTT client's ability to connect and disconnect from the broker.
		"""
		delay = self.cfg.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.KEEP_ALIVE_KEY, ConfigConst.DEFAULT_KEEP_ALIVE)
		self.mcc.connectClient()
		sleep(delay + 5)
		self.mcc.disconnectClient()
		
	#@unittest.skip("Ignore for now.")
	def testConnectAndCDAManagementStatusPubSub(self):
		"""
		Test publishing and subscribing to the CDA management status message resource.
		"""
		qos = 1
		delay = self.cfg.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.KEEP_ALIVE_KEY, ConfigConst.DEFAULT_KEEP_ALIVE)
		self.mcc.connectClient()
		self.mcc.subscribeToTopic(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, qos = qos)
		sleep(5)
		self.mcc.publishMessage(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, msg = "TEST: This is the CDA message payload.", qos = qos)
		sleep(5)
		self.mcc.unsubscribeFromTopic(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE)
		sleep(5)
		sleep(delay)
		self.mcc.disconnectClient()
	
	#@unittest.skip("Ignore for now.")
 
	def testNewActuatorCmdPubSub(self):
		"""
		Test publishing a new actuator command.
		"""
		qos = 1
		# NOTE: delay can be anything you'd like - the sleep() calls are simply to slow things down a bit for observation
		delay = self.cfg.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.KEEP_ALIVE_KEY, ConfigConst.DEFAULT_KEEP_ALIVE)
		actuatorData = ActuatorData()
		payload = DataUtil().actuatorDataToJson(actuatorData)
		self.mcc.setDataMessageListener(DefaultDataMessageListener())
		
		logging.info("Sample ActuatorData JSON (validated): " + str(payload))
		
		self.mcc.connectClient()
		sleep(5)
		self.mcc.publishMessage(resource = ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE, msg = payload, qos = qos)
		sleep(delay)
		self.mcc.disconnectClient()
		
		
	#@unittest.skip("Ignore for now.")
	def testActuatorCmdPubSub(self):
		"""
		Test publishing actuator command and setting a specific command value.
		"""
		qos = 0
		
		delay = self.cfg.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.KEEP_ALIVE_KEY, ConfigConst.DEFAULT_KEEP_ALIVE)
		
		actuatorData = ActuatorData()
		actuatorData.setCommand(7)
		
		
		
		self.mcc.setDataMessageListener(DefaultDataMessageListener())
		payload = DataUtil().actuatorDataToJson(actuatorData)
		self.mcc.connectClient()
		sleep(5)
		self.mcc.publishMessage(resource = ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE, msg = payload, qos = qos)
		sleep(delay + 5)
		self.mcc.disconnectClient()
	#@unittest.skip("Ignore for now.")
	def testSensorMsgPub(self):
		"""
		Test publishing sensor data.
		"""
		qos = 0
		delay = self.cfg.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.KEEP_ALIVE_KEY, ConfigConst.DEFAULT_KEEP_ALIVE)
		sensorData = SensorData()
		sensorData.setValue(22.0)
		self.mcc.setDataMessageListener(DefaultDataMessageListener())
		payload = DataUtil().sensorDataToJson(sensorData)
		self.mcc.connectClient()
		sleep(5)
		self.mcc.publishMessage(resource = ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, msg = payload, qos = qos)
		sleep(delay + 5)
		self.mcc.disconnectClient()
	#@unittest.skip("Ignore for now.")
	def testCDAManagementStatusSubscribe(self):
		"""
		Test subscribing to the CDA management status command resource.
		"""
		qos = 1
		delay = self.cfg.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.KEEP_ALIVE_KEY, ConfigConst.DEFAULT_KEEP_ALIVE)
		self.mcc.connectClient()
		self.mcc.subscribeToTopic(resource = ResourceNameEnum.CDA_MGMT_STATUS_CMD_RESOURCE, qos = qos)
		sleep(delay)
		self.mcc.disconnectClient()
	#@unittest.skip("Ignore for now.")
	def testCDAActuatorCmdSubscribe(self):
		"""
		Test subscribing to the CDA actuator command resource.
		"""
		qos = 1
		delay = self.cfg.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.KEEP_ALIVE_KEY, ConfigConst.DEFAULT_KEEP_ALIVE)
		self.mcc.connectClient()
		self.mcc.subscribeToTopic(resource = ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE, qos = qos)
		sleep(300)
		self.mcc.disconnectClient()
	#@unittest.skip("Ignore for now.")
	def testCDAManagementStatusPublish(self):
		"""
		Test publishing a message to the CDA management status message resource.
		Note: Uncomment this test for integration between GDA and CDA using MQTT.
		"""
		qos = 1
		delay = self.cfg.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.KEEP_ALIVE_KEY, ConfigConst.DEFAULT_KEEP_ALIVE)
		self.mcc.connectClient()
		self.mcc.publishMessage(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, msg = "TEST: This is the CDA message payload.", qos = qos)
		sleep(delay)
		self.mcc.disconnectClient()
if __name__ == "__main__":
	unittest.main()