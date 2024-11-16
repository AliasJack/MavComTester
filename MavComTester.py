from pymavlink import mavutil
import time

print("connecting to mavlink on pixhawk")
gcs_connection = mavutil.mavlink_connection('udpout:localhost:14540')

time.sleep(0.2)
global boot_time
boot_time = time.time()
while 1:
    time.sleep(1)
    gcs_connection.mav.heartbeat_send(
        6, #MAVTYPE = 
        8, #MAVAUTOPILOT
        128, # MAV_MODE = 
        0,0) #MAVSTATE =
    print("SEND HEARBEAT")
