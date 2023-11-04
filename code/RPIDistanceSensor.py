import requests
import http.client
import json
import ssl
import re, subprocess 
import os , time
from rangesensor import *
 
def read_cpuTemp():
	temp = None 
	temp = os.popen('vcgencmd measure_temp').readline()
	temp = temp[5:9]
	print (temp) 
	return temp


ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)
ssl_context.minimum_version = ssl.TLSVersion.TLSv1_2

# note the use of ALPN
ssl_context.set_alpn_protocols(["x-amzn-http-ca"])
ssl_context.load_verify_locations(cafile="Amazon-root-CA-1.pem")

# update the certificate and the AWS endpoint
ssl_context.load_cert_chain("device.pem.crt", "private.pem.key")
connection = http.client.HTTPSConnection('a256qtpnm2ka1u-ats.iot.eu-central-1.amazonaws.com', 443, context=ssl_context)

i = 0
while i < 10:
	distance = calculate_distance()
	temp = read_cpuTemp()
	message = {'Temp': temp,'Range': distance, "device_id":"RPI1","Location":"Bangalore"}

	#message = {'Temp': '28.4','Message':'Message from RPI','Remark':'Message from RPI by Shailendra on 1St November - Happy Birthday Ranjan Sir'}
	json_data = json.dumps(message)

	# Correct the topic in the URL
	url = '/topics/topic/rpi/temp?qos=1'
	headers = {'Content-Type': 'application/json'}

	connection.request('POST', url, json_data, headers=headers)

	# make request
	response = connection.getresponse()

	# print results
	print(response.read().decode())
	
	i +=1
	time.sleep(5)
