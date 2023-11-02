#this code use curl command inside the python code. 

import subprocess
import time
import random 

def get_temperature_sensor_value():
    # Read the temperature sensor
    temperature_sensor_value = random.uniform(20, 35)

    # Return the temperature sensor value
    return temperature_sensor_value


# Start a loop to publish the temperature sensor value every second
while True:

    temperature_sensor_value = get_temperature_sensor_value()
    print(temperature_sensor_value) 

    # Set the curl command
    curl_command = "curl --tlsv1.2 --cacert Amazon-root-CA-1.pem --cert device.pem.crt --key private.pem.key --request POST --data '{ \"Temp\": \"$temperature_sensor_value\" }' https://a256qtpnm2ka1u-ats.iot.eu-north-1.amazonaws.com:8443/topics/topic?qos=1"


    # Replace the string "$temperature_sensor_value" with the actual random value of temperature
    curl_command = curl_command.replace("$temperature_sensor_value", str(temperature_sensor_value))

    # Run the curl command
    subprocess.run(curl_command, shell=True)

    # Wait for 1 second
    time.sleep(5)