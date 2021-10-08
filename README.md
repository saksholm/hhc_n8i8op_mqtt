# hhc_n8i8op_mqtt
HHC-N8I8OP MQTT gateway. Publish your relay board as MQTT topic tree. Can support several boards at same time. Connects to MQTT broker at localhost, default server port.
You have to set your HHC-N8I8OP as UDP service, port 5000.
https://es.aliexpress.com/item/4000120026245.html


# modified version setup:
- rename default_config.yaml to config.yaml and change values
- rename default_inventory.yaml to inventory.yaml and config values


### usage:

####command topic:
set relay 1:
- iot/relay_board_1/1/state/set -> "ON" or "OFF"


####state topic:
read relay 2:
- iot/relay_board_1/2/state -> "ON" or "OFF"