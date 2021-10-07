#!/bin/bash
mosquitto_pub -t "iot/garage_relay_$1/relay_$2/state/set" -m "$3"
