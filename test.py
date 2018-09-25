import json
import requests

#url = "http://217.33.61.83:8585/api/2/things"
url = "http://localhost"

msg = b'{"node_id":"16700204541000610066a000a00000c1","ts":1537801843459,"phase_1_voltage_rms":234.58,"phase_2_voltage_rms":234.56,"phase_3_voltage_rms":234.16,"phase_1_current_rms":0.93,"phase_2_current_rms":0.99,"phase_3_current_rms":0.26,"n_line_calculated_current_rms":1.99,"phase_1_frequency":50,"phase_2_voltage_phase":0,"phase_3_voltage_phase":119.6,"phase_1_voltage_thd_n":3.97,"phase_2_voltage_thd_n":3.97,"phase_3_voltage_thd_n":5.23,"phase_1_current_thd_n":114.45,"phase_2_current_thd_n":109.35,"phase_3_current_thd_n":11.62,"phase_1_active_power":131,"phase_2_active_power":143,"phase_3_active_power":21,"phase_1_reactive_power":-54,"phase_2_reactive_power":-52,"phase_3_reactive_power":-52,"phase_1_apparent_power":218,"phase_2_apparent_power":231,"phase_3_apparent_power":60,"phase_1_power_factor":0.6,"phase_2_power_factor":0.62,"phase_3_power_factor":0.35,"phase_1_active_fundamental":134,"phase_2_active_fundamental":146,"phase_3_active_fundamental":21,"phase_1_active_harmonic":-3,"phase_2_active_harmonic":-3,"phase_3_active_harmonic":0,"phase_1_forward_active":0.02,"phase_2_forward_active":0.02,"phase_3_forward_active":0,"phase_1_reverse_active":0,"phase_2_reverse_active":0,"phase_3_reverse_active":0,"phase_1_forward_reactive":0,"phase_2_forward_reactive":0,"phase_3_forward_reactive":0,"phase_1_reverse_reactive":0.01,"phase_2_reverse_reactive":0.01,"phase_3_reverse_reactive":0.01,"phase_1_apparent_energy":0.03,"phase_2_apparent_energy":0.03,"phase_3_apparent_energy":0.01,"measured_temperature":35,"input_1_status":0,"input_2_status":0,"input_3_status":0}'

units = ["V", "V", "V", "A", "A", "A", "A", "Hz", "deg", "deg", "%", "%", "%", "%", "%", "%", "W", "W", "W", "kvar", "kvar", "kvar", "VA", "VA", "VA", "No_Unit", "No_Unit", "No_Unit", "W", "W", "W", "W", "W", "W", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "Wh", "degC"]

data = json.loads(msg.decode('utf-8'))
node_id = "org.nrg5:" + data["node_id"]
ts = data["ts"]
del data["node_id"]
del data["ts"]
del data["input_1_status"]
del data["input_2_status"]
del data["input_3_status"]

nrg5_msg = {"thingId": node_id}
nrg5_msg["policyId"] = node_id
nrg5_msg["attributes"] = {"firmware":"v1.0","software":"v1.0","manufacturer":"JSI"}
nrg5_msg["timestamp"] = ts
nrg5_msg["features"] = {}


for i,field in enumerate(data):
    nrg5_msg["features"][field] = {"value": float(data[field]), "units": units[i]}

#r = requests.put(url, json=nrg5_msg)
#print(r.text)

print(json.dumps(nrg5_msg))