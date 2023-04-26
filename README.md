# CPE314-IOT:Computer Networks
Project CPE314 IOT
IOT will have 4 parts that is Client, Broker, Server and Database. Client will send data to Broker. Then Broker will send data to Server. Finally, Server will send data to create table in Database to save all data.

This folder have 3 files for python and 1 file Node-red
1. Readme : Describing what each file is.
2. Publish.py : Client file to connect MQTT Broker and Send data to MQTT Broker.
3. Subscribe.py :Server file to connect MQTT Broker and Database, call received data, send data Database and show data that server will send in server.
4. Mqtt.json : IOT simulate by Node-Red  

How to use:
Python
1. สร้าง server ของ MQTT Broker เพื่อนำ host, port, username, password มาใช้เชื่อมต่อของ Client and Server #ติดตั้ง Mosquitto และ MQTT-Explorer
2. สร้างตารางใน Database #ใช้ pgAdmin : มีข้อมูล node_id(char 250), time_sent(char 250), humidity(char 250), temperature(char 250) และ thermal_array(่json[])
3. connect MQTT-Explorer
3. เรียกใช้ไฟล์ Python ด้วยคำสั่ง python namefile.py โดยเรียกใช้ 2 ไฟล์เพื่อเชื่อม Client ไปยัง MQTT Broker และเชื่อม Server ไป MQTT Broker :
   - python publish.py
   - python subscribe.py
4. พิมพ์ส่งข้อมูลด้วย publish.py 
5. ถ้าต้องการออกจากการเชื่อมต่อสามารถกด CTRL+C ทั้ง 2 ไฟล์

Node-Red
- Import Mqtt.json เข้า Node-red จะสามารถใช้งานทั้งหมดได้ใน Node-red แต่จำเป็นที่จะต้องเปิดและเชื่อมต่อทั้ง Hivemq และ MySQL จาก XAMPP Control Panel
