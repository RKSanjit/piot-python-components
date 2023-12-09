# Constrained Device Application (Connected Devices)


## Lab Module 06


### Description

This implementation adds MQTT messaging capabilities to the Constrained Device Application (CDA) to enable publish/subscribe communication with other applications.The CDA can now connect to an MQTT broker, publish sensor data and status messages to specified topics, and subscribe to topics in order to receive incoming actuation commands. The Eclipse Paho MQTT Python client library is used to handle the MQTT protocol details.

Callbacks have been implemented to process connect/disconnect events and receive messages from subscribed topics. The MQTT client is initialized and connected/disconnected within the DeviceDataManager class.

When starting up, the CDA subscribes to an "Actuator Commands" topic in order to receive any actuation directives. The CDA can now publish sensor messages to separate sensor data and status topics periodically based on configuration.

This allows the CDA to integrate with other applications like the Gateway Device Application (GDA) using asynchronous, event-driven MQTT messaging. The publish/subscribe model facilitates flexible integration without direct dependencies between the applications.

### Code Repository and Branch

URL: https://github.com/RKSanjit/piot-python-components/tree/labmodule06

### UML Design Diagram(s)

![mod6 ](https://github.com/RKSanjit/book-exercise-docs/assets/144634185/845058d5-9629-4496-849e-51d1fa84a874)



### Integration Tests Executed

- MqttClientConnectorTest





=======
## Lab Module 09

### Description

This implementation integrates a CoAP client into the Constrained Device Application (CDA) using the Coapthon3 library. It allows the CDA to communicate with the Gateway Device Application's (GDA) CoAP server using CoAP request/response messaging.

The CoAP client functionality is handled by the CoapClientConnector class, which provides an adapter to the Coapthon3 library. The client can send CoAP GET and PUT requests to submit sensor data to the GDA and receive actuator commands. It also supports CoAP observations to wait for updates from the GDA instead of polling. The connector methods convert data between Python objects and JSON strings to interface with the GDA's data types. Callbacks route responses to the appropriate handlers. Overall, the CoAP client built on Coapthon3 enables integration between the CDA and GDA using CoAP for sending telemetry and receiving actuator commands.

### Code Repository and Branch

URL: https://github.com/RKSanjit/piot-python-components/blob/labmodule09

### UML Design Diagram(s)
![mod9](https://github.com/RKSanjit/book-exercise-docs/assets/144634185/607bf31e-d5fe-4503-afc3-736fd51a1282)

### Integration Tests Executed

- CoapClientConnectorTest 


>>>>>>> labmodule09
EOF.
