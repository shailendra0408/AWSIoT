import requests
import http.client
import json
import ssl

ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)
ssl_context.minimum_version = ssl.TLSVersion.TLSv1_2

# note the use of ALPN
ssl_context.set_alpn_protocols(["x-amzn-http-ca"])
ssl_context.load_verify_locations(cafile="Amazon-root-CA-1.pem")

# update the certificate and the AWS endpoint
ssl_context.load_cert_chain("device.pem.crt", "private.pem.key")
connection = http.client.HTTPSConnection('a256qtpnm2ka1u-ats.iot.eu-north-1.amazonaws.com', 443, context=ssl_context)

# add the QoS header
headers = {"QoS": "1"}

message = {'Temp': '28.4'}
json_data = json.dumps(message)
connection.request('POST', '/topics/topic%2Fmessage?qos=1', json_data, headers=headers)

# make request
response = connection.getresponse()

# print results
print(response.read().decode())