import unittest
import logging
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.cda.connection.RedisPersistenceAdapter import RedisPersistenceAdapter

class RedisClientAdapterTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO)
        cls.logger = logging.getLogger("RedisClientAdapterTest")
        cls.logger.info("Testing RedisClientAdapterTest class started.")

    def setUp(self):
        """
        Set up resources before each test
        """
        self.redisPersistenceAdapter = RedisPersistenceAdapter()
        self.logger.info("Set up RedisPersistenceAdapter for testing.")

    def tearDown(self):
        """
        Clean up resources after each test
        """
        self.redisPersistenceAdapter.disconnectClient()
        self.logger.info("Cleaned up RedisPersistenceAdapter after testing.")

    def testConnectClient(self):
        """
        Test the connectClient method
        """
        self.logger.info("Testing connectClient method.")
        success = self.redisPersistenceAdapter.connectClient()
        self.assertTrue(success, "Failed to connect to Redis server.")
        self.logger.info("connectClient method test passed.")

    def testDisconnectClient(self):
        """
        Test the disconnectClient method
        """
        self.logger.info("Testing disconnectClient method.")
        self.redisPersistenceAdapter.connectClient()
        success = self.redisPersistenceAdapter.disconnectClient()
        self.assertTrue(success, "Failed to disconnect from Redis server.")
        self.logger.info("disconnectClient method test passed.")

    def testStoreSensorData(self):
        """
        Test storing SensorData to Redis
        """
        self.logger.info("Testing storeSensorData method.")
        self.redisPersistenceAdapter.connectClient()
        sensor_data = SensorData()
        # You can set up sensor_data with specific values if needed
        success = self.redisPersistenceAdapter.storeData(ResourceNameEnum.SENSOR_DATA, sensor_data)
        self.assertTrue(success, "Failed to store SensorData in Redis.")
        self.logger.info("storeSensorData method test passed.")

    @classmethod
    def tearDownClass(cls):
        cls.logger.info("Testing RedisClientAdapterTest class completed.")

if __name__ == "__main__":
    unittest.main()
