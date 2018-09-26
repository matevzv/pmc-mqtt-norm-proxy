#!/usr/bin/env python3

import json
import requests
import paho.mqtt.client as mqtt

url = "http://217.33.61.83:8585/api/2/things/"

pmcs = [("pmc/1670020454100061004aa000a0000005",0), ("pmc/16700204541000610080a000a000007d",0), ("pmc/16700204541000610088a000a0000045",0)]

units = ["V", "V", "V", "A", "A", "A", "A", "Hz", "deg", "deg", "%", "%", "%", "%", "%", "%", "W", "W", "W", "kvar", "kvar", "kvar", "VA", "VA", "VA", "No_Unit", "No_Unit", "No_Unit", "W", "W", "W", "W", "W", "W", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "degC"]

def on_connect(mqttc, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    mqttc.subscribe(pmcs)

def on_message(mqttc, userdata, msg):
    data = json.loads(msg.payload.decode('utf-8'))

    node_id = data["node_id"]
    norm_id = "org.nrg5:" + node_id
    ts = data["ts"]
    del data["node_id"]
    del data["ts"]
    del data["input_1_status"]
    del data["input_2_status"]
    del data["input_3_status"]

    norm_msg = {"thingId": norm_id}
    norm_msg["policyId"] = norm_id
    norm_msg["attributes"] = {"firmware":"v1.0","software":"v1.0","manufacturer":"JSI"}
    norm_msg["timestamp"] = ts
    norm_msg["features"] = {}

    for i,field in enumerate(data):
        norm_msg["features"][field] = {"value": float(data[field]), "units": units[i]}

    requests.put(url+norm_id, json=norm_msg, auth=('ditto', 'ditto'))

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect("localhost")

mqttc.loop_forever()
