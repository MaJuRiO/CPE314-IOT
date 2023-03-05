#publish or client will have 3 parts. 
#1. Setting MQTT Broker.
#2. Connecting function to MQTT Broker.
#3. Publish function to send data to MQTT Broker. 
from paho.mqtt import client as mqtt_client
import random
import time
#Setting mqtt broker
mqtt_host = "localhost"
mqtt_port = 1883
mqtt_username = "mqtt"
mqtt_password = "Majuandfriends"
mqtt_topic = "sensor/data"
client_id = f'python-mqtt-{random.randint(0, 1000)}' #use client_id by random

#connect to mqtt broker
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        #method to check connection
        if rc == 0:
            print("Connected to MQTT Broker!")
            print(client_id," is connected.")
        else:
            print("Failed to connect, return code %d\n", rc)
    #set client id to connect
    client = mqtt_client.Client(client_id)
    client.username_pw_set(mqtt_username, mqtt_password)
    client.on_connect = on_connect
    client.connect(mqtt_host, mqtt_port)
    return client
#function to send data from client to mqtt broker
def publish(client):
    msg_count = 0
    while True:
        time.sleep(1) #delay when a set of data will send 
        msg = f"messages: {msg_count}" #count set of data 
        #simulate sensor data transmission by input data
        time_sent = input('Enter the Time sent (maximum 250 bytes):') 
        humidity = input('Enter the Humidity (maximum 250 bytes):')
        temperature = input('Enter the Temperature (maximum 250 bytes):')
        thermal_array = input('Enter the Thermal Array (maximum 250 bytes):')
        result=[time_sent,humidity,temperature,thermal_array,msg] #get data to list
        #send data to mqtt broker
        client.publish(mqtt_topic,result[0])
        client.publish(mqtt_topic,result[1])
        client.publish(mqtt_topic,result[2])
        client.publish(mqtt_topic,result[3])
        print(f"Send {msg} to topic {mqtt_topic}")
        msg_count += 1

#function to run operation all file
def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()