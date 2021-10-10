# hhc_n8i8op_mqtt
HHC-N8I8OP MQTT gateway. Publish your relay board as MQTT topic tree. Can support several boards at same time. Connects to MQTT broker at localhost, default server port.
You have to set your HHC-N8I8OP as UDP service, port 5000.
https://es.aliexpress.com/item/4000120026245.html


# modified version setup:
First clone this repo.
run ``python3 setup.py`` or:
- rename ``default_config.yaml`` to ``config.yaml``
- rename ``default_inventory.yaml`` to ``inventory.yaml``

change values of config and inventory files


## usage:

start script: ``python3 relay_manager.py``



#### command topic:
set relay 1:
- ``iot/relay_board_1/1/state/set`` -> ``ON`` or ``OFF``


#### state topic:
read relay 2:
- ``iot/relay_board_1/2/state`` -> ``ON`` or ``OFF``


# Run script on PM2 process manager

- Simply install first PM2
- ``cd hhc_n8i8op_mqtt``
- run ``pm2 start relay_manager.py --name relay_manager --interpreter python3``
- When you tested that everything is running smoothly. Enter command: ``pm2 startup`` and follow instructions. Script is running now on your server properly after server restarts or script fails.

Side note! When you update pm2 or python you may need to run ``pm2 startup`` again.
