import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import ticket_checker

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN


last_data_object = ""
last_result = ""
while True:
    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        ticket_data = str(obj.data,"utf-8").strip()
        if(ticket_data==last_data_object):
            print("Same Data!")
            color = (255,0,0) if result == "Valid Ticket" else (0,0,255)
            cv2.putText(frame, result, (300, 200), font, 3,
                        color, 3)
        else:
            print("New Data!")

            last_data_object = ticket_data
            result = ticket_checker.check_in(ticket_data)
            print("Result: ",result)
            last_result = result
            print("Data", obj.data)
            color = (255, 0, 0) if result == "Valid Ticket" else (0, 0, 255)
            cv2.putText(frame, result, (300, 200), font, 3,
                        color, 3)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break