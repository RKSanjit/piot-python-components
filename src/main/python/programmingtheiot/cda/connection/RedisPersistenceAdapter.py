import logging
import redis

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.DataUtil import DataUtil

class RedisPersistenceAdapter(object):
    """
    Class to facilitate connection to the Redis database for storage and retrieval of system, sensor, and actuator data.
    """

    def __init__(self):
        logging.info("RedisPersistenceAdapter instantiated.")
        configUtil = ConfigUtil()
        self.host = configUtil.getProperty(section=ConfigConst.DATA_GATEWAY_SERVICE, key=ConfigConst.HOST_KEY, defaultVal=ConfigConst.DEFAULT_HOST)
        self.port = configUtil.getInteger(section=ConfigConst.DATA_GATEWAY_SERVICE, key=ConfigConst.PORT_KEY, defaultVal=ConfigConst.DEFAULT_DATA_PORT)
        self.connectStatus = False
        self.dbClient = redis.Redis(host=self.host, port=self.port, db=0, decode_responses=True)
        self.connectStatus = self.connectClient()
        self.index = 1

        if self.connectStatus:
            logging.info("Redis connect successful.")
        else:
            logging.warning("Redis connection was not successful.")

    def connectClient(self) -> bool:
        """
        Attempts to start the Redis client.
        @return boolean: Denotes the success of the operation.
        """
        try:
            self.dbClient.ping()
            logging.debug("Redis CheckConnectedStatus passed.")
            return True
        except redis.exceptions.RedisError as e:
            logging.error("Redis CheckConnectedStatus failed: %s", str(e))
            return False

    def disconnectClient(self) -> bool:
        """
        Attempts to stop the Redis client.
        @return boolean: Denotes the success of the operation.
        """
        if self.connectStatus:
            logging.info("Disconnecting from Redis")
            try:
                self.dbClient.connection_pool.disconnect()
                self.connectStatus = False
                logging.info("Disconnected from Redis")
                return True
            except redis.exceptions.RedisError as e:
                logging.error("Error disconnecting from Redis: %s", str(e))
                return False
        else:
            logging.info("Redis is already disconnected.")
            return True

    def storeData(self, resource: ResourceNameEnum, data: SensorData) -> bool:
        """
        Attempts to store data in the Redis database.
        @param resource: The reference topic used to store the data.
        @param data: The SensorData to be stored.
        @return boolean: Denotes the success or failure of the operation.
        """
        if resource and data:
            du = DataUtil(True)
            try:
                json_obj = du.sensorDataToJson(data)
                day = data.getTimeStamp().replace("-", "T").split("T")
                topic = resource.value + '/' + str(day[2]) + '/' + str(self.index)
                
                self.dbClient.set(topic, json_obj)
                logging.info("Data stored in database successfully: " + topic)
                self.index += 1
                return True
            except redis.exceptions.RedisError as e:
                logging.error("Data storage unsuccessful: %s", str(e))
                return False
        else:
            logging.info("Storage unsuccessful: Resource name or data is null")
            return False
