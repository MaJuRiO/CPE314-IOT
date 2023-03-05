#Subscribe.py or Server will have 4 parts.
#1. Setting MQTT Broker and Database.
#2. Connecting MQTT Broker.
#3. Received Function to call data from MQTT Broker.
#4. Database Function to send data and show data.
from paho.mqtt import client as mqtt_client
import random
import psycopg2 
import psycopg2.extras
#Setting mqtt broker and Database
#MQTT Broker
mqtt_host = "localhost"
mqtt_port = 1883
mqtt_username = "mqtt"
mqtt_password = "Majuandfriends"
mqtt_topic = "sensor/data"
client_id = f'python-mqtt-{random.randint(0, 1000)}' #use client_id by random
node_id = client_id
#Database
host = "127.0.0.1"
user = "postgres"
password = "1234"
db = "cpe314"

#connect to mqtt broker
def connect_mqtt() :
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

#Connecting database (use by pgAdmin4)
conn = psycopg2.connect(host=host, user=user, password=password, database=db)
cur = conn.cursor()
final = [] #variable of get all data that received.

#Received function to call receive data from mqtt broker
def subscribe(client: mqtt_client):
    #function to call and show data that received 
    def on_message(client, userdata, result):
        print(f"Received `{result.payload.decode()}` from `{result.topic}` topic") #show data
        #get data to new list
        data = result.payload.decode()
        final.append(data)
        #Method to chek all data will receive and send to database
        if(len(final)>=4):
            database(final)

    client.subscribe(mqtt_topic)
    client.on_message = on_message
    #function to send data to Database and show data in server
    def database(data):
        final = data
        cur.execute("INSERT INTO iot (node_id, time_sent, humidity, temperature, thermal_array) VALUES ('{}', '{}', '{}', '{}', '{}')".format(node_id, final[0], final[1],final[2],final[3])) #Insert data into iot table of database
        conn.commit()
        #Show all data in database
        cur.execute("SELECT * FROM iot ") 
        query = cur.fetchall()
        for i in query:
            print(i)

#function to run operation all file
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()

