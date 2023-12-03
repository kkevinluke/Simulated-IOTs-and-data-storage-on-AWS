!pip install AWSIoTPythonSDK

import json
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# Define parameters
humidity = 60.5
temperature = 25.8
wind_speed = 15.2
ship_speed = 30
cloud_density = 70
visibility = 90
ocean_floor_depth = 1500
time_now = "13:45:00"
date_today = "2023-12-01"
latitude = 40.7128
longitude = -74.0060
ship_health = "good"
electrical_status = "normal"
fuel_level = 75
cargo_weight = 5000
start_time = "08:00:00"
start_destination = "Port A"
end_time = "17:00:00"
end_destination = "Port B"
mid_stop_location_time = "11:30:00"
mid_stop_location_name = "Port C"
mid_start_location_time = "14:30:00"
mid_start_location_name = "Port D"

# Prepare sensor data as JSON payload
sensor_data = {
    "humidity": humidity,
    "temperature": temperature,
    "wind_speed": wind_speed,
      "ship_speed": ship_speed,
    "cloud_density": cloud_density,
    "visibility": visibility,
    "ocean_floor_depth": ocean_floor_depth,
    "time": time_now,
    "date": date_today,
    "latitude": latitude,
    "longitude": longitude,
    "ship_health": ship_health,
    "electrical_status": electrical_status,
    "fuel_level": fuel_level,
    "cargo_weight": cargo_weight,
    "start_time": start_time,
    "start_destination": start_destination,
    "end_time": end_time,
    "end_destination": end_destination,
    "mid_stop_location_time": mid_stop_location_time,
    "mid_stop_location_name": mid_stop_location_name,
    "mid_start_location_time": mid_start_location_time,
    "mid_start_location_name": mid_start_location_name
  
}
    
# Convert to JSON format
payload = json.dumps(sensor_data)

# AWS IoT Core configuration
myMQTTClient = AWSIoTMQTTClient("iotconsole-7509170a-5685-41a7-a977-9764c3fce79c")  # Replace with your chosen client ID
myMQTTClient.configureEndpoint("a3peg7ssvhzi2u-ats.iot.eu-west-1.amazonaws.com", 8883)  # Replace with your AWS IoT endpoint
myMQTTClient.configureCredentials(r"D:\Data_Science\PhD\Tests\AmazonRootCA1.pem", r"D:\Data_Science\PhD\Tests\15561d224a055e88b05e965bb32ebed6ee498ee562a14eab8db6e3ddf1d2f049-private.pem.key", r"D:\Data_Science\PhD\Tests\15561d224a055e88b05e965bb32ebed6ee498ee562a14eab8db6e3ddf1d2f049-certificate.pem.crt")

# Connect to AWS IoT Core
myMQTTClient.connect()

    
# Publish data to a specific topic
myMQTTClient.publish("ship1", payload, 1)



# Disconnect from AWS IoT Core
myMQTTClient.disconnect()


!ping a3peg7ssvhzi2u-ats.iot.eu-west-1.amazonaws.com #iot_endpoint

