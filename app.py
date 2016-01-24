#!flask/bin/python
from flask import Flask, jsonify, abort
from random import randint

app = Flask(__name__)

SensorList = [
    {
        'Sensorid': 1,
        'SensorName': u'Temp Sensor',
        'description': u'Temp Sensor  1', 
        'RelayStatusFlag': True,
        'SensorValue': randint(1,200)
    },
    {
        'Sensorid': 2,
        'SensorName': u'Moisture Sensor',
        'description': u'Moisture Sensor 1', 
        'RelayStatusFlag': False,
        'SensorValue': randint(1,200)
    },
    {
        'Sensorid': 3,
        'SensorName': u'Humidity Sensor',
        'description': u'Humidity Sensor 1', 
        'RelayStatusFlag': False,
        'SensorValue': randint(1,200)
    }
]

@app.route('/getsensorval/<int:sensor_id>', methods=['GET'])
def get_SensorId(sensor_id):
	AbortFlag = True
	for SensID in SensorList:
		#print SensID['Sensorid']
		if(SensID['Sensorid'] == sensor_id):
			print SensID['Sensorid']
			AbortFlag = False
			return jsonify({'SensorDisplay': SensID})
	if(AbortFlag == True):
		abort(404)
"""
    SensID = [SensID for SensID in SensorList if SensID['Sensorid'] == sensor_id]
    if len(SensID) == 0:
        abort(404)
    return jsonify({'task': Sensorid[0]})
"""

@app.route('/getsensorval', methods=['GET'])
def get_SensorVals():
    return jsonify({'SensorList': SensorList})

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
