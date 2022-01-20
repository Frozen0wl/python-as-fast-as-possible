import krpc
import time

connection = krpc.connect()

vessel = connection.space_center.active_vessel

time.sleep(2)

vessel.control.activate_next_stage()

reffname = vessel.orbit.body.reference_frame

position = connection.add_stream(vessel.position, reffname)

while True:
    print (position())
