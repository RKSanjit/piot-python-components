# Constrained Device Application (Connected Devices)

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


EOF.
