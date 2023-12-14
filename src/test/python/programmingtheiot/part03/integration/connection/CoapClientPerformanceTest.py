import logging
import time
import unittest
from time import sleep
from threading import Semaphore

from programmingtheiot.cda.connection.CoapClientConnector import CoapClientConnector
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.data.DataUtil import DataUtil
from programmingtheiot.data.SensorData import SensorData

class CoapClientPerformanceTest(unittest.TestCase):
    """
    This test case class contains very basic performance tests for
    CoapClientConnector. It should not be considered complete,
    but serves as a starting point for implementing
    additional functionality within their Programming the IoT
    environment.
    """
    NS_IN_MILLIS = 1000000
    MAX_TEST_RUNS = 10000
    CONCURRENCY_LEVEL = 5  # Limit the number of concurrent requests

    @classmethod
    def setUpClass(self):
        logging.disable(level = logging.WARNING)
        self.semaphore = Semaphore(self.CONCURRENCY_LEVEL)

        
    def setUp(self):
        self.coapClient = CoapClientConnector()

    def tearDown(self):
        self.coapClient.disconnectClient()
                    
    #@unittest.skip("Ignore for now.")
    def testPostRequestCon(self):
        print("Testing POST - CON")
        
        self._execTestPost(self.MAX_TEST_RUNS, True)
        
    #@unittest.skip("Ignore for now.")
    def testGetRequestNon(self):
        print("Testing GET - NON")
        self._execTestGet(self.MAX_TEST_RUNS, False)

  #  @unittest.skip("Ignore for now.")
    def testPostRequestNon(self):
        print("Testing POST - NON")
        self._execTestPost(self.MAX_TEST_RUNS, False)

    def testPutRequestCon(self):
        print("Testing PUT - CON")
        self._execTestPut(self.MAX_TEST_RUNS, True)

    def testPutRequestNon(self):
        print("Testing PUT - NON")
        self._execTestPut(self.MAX_TEST_RUNS, False)

    def _execTestGet(self, maxTestRuns: int, useCon: bool):
        startTime = time.time_ns()
        for seqNo in range(0, maxTestRuns):
            with self.semaphore:
                self.coapClient.sendGetRequest(resource=ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE, enableCON=useCon)
                sleep(0.5)  # Introduce a slight delay
        endTime = time.time_ns()
        elapsedMillis = (endTime - startTime) / self.NS_IN_MILLIS
        print("\nGET message - useCON = " + str(useCon) + " [" + str(maxTestRuns) + "]: " + str(elapsedMillis) + " ms")

    def _execTestPost(self, maxTestRuns: int, useCon: bool):
            sensorData = SensorData()
            payload = DataUtil().sensorDataToJson(sensorData)
            
            startTime = time.time_ns()
            
            for seqNo in range(0, maxTestRuns):
                self.coapClient.sendPostRequest(resource = ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, enableCON = useCon, payload = payload)
                
            endTime = time.time_ns()
            elapsedMillis = (endTime - startTime) / self.NS_IN_MILLIS
            
            print("POST message - useCON = " + str(useCon) + " [" + str(maxTestRuns) + "]: " + str(elapsedMillis) + " ms")

    def _execTestPut(self, maxTestRuns: int, useCon: bool):
        sensorData = SensorData()
        payload = DataUtil().sensorDataToJson(sensorData)
        startTime = time.time_ns()
        for seqNo in range(0, maxTestRuns):
            with self.semaphore:
                self.coapClient.sendPutRequest(resource=ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, enableCON=useCon, payload=payload)
                sleep(0.5)  # Introduce a slight delay
        endTime = time.time_ns()
        elapsedMillis = (endTime - startTime) / self.NS_IN_MILLIS
        print("\nPUT message - useCON = " + str(useCon) + " [" + str(maxTestRuns) + "]: " + str(elapsedMillis) + " ms")

if __name__ == "__main__":
    unittest.main()
