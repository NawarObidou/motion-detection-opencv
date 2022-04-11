# prototype code

# This is the code that makes the live monitoring system work
# an important note to make about the camera feed
# the counter is inaccurate
# noise detection has been minimised as much as possible
 
# import necessary libraries
from tkinter import *
import cv2
import numpy as np

cap = cv2.VideoCapture(00)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

# widgets and labels on the GUI
root = Tk()
root.config(bg='SteelBlue1')
root.title('Monitoring system')

mainWindow = Frame(root)


Label1 = Label(root, text='Live Monitoring System Initial Prototype', bg='SteelBlue1', pady=10, padx=30, font=('Courier', 10))
Label1.grid(row=0, column= 0)

mainLbl = Label(mainWindow)
mainLbl.grid()


# the function that activates the camera and recording
def camActivate():
    capture = cv2.VideoCapture(0)
    ret, frame1 = capture.read()
    ret, frame2 = capture.read()

    # code that saves the file
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('Latest Recording.avi', fourcc, 20.0, (640, 480))

    while capture.isOpened():
        ret, frame = capture.read()
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        cv2.putText(frame1, 'Recording', (00, 450),
                    cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
        cv2.putText(frame1, 'Press ESC to Exit', (250, 450),
                    cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
        cv2.circle(frame1, (190, 440), 20, (0, 0, 255), -1)

        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2image = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)

        # code that decides the threshold for movement detection, text and visual alerts
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 4500:
                continue
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame1, 'Movement', (200, 20),
                        cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 1)

            cv2.putText(frame1, str(len(contour)), (500, 20),
                        cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 1)

            cv2.circle(frame1, (190, 440), 20, (0, 255, 0), -1)

        # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
        cv2.imshow('Live Camera Feed', frame1)
        frame1 = frame2
        ret, frame2 = capture.read()
        if cv2.waitKey(40) == 27:
            break
    out.release()
    capture.release()
    cv2.destroyAllWindows()

# the two buttons on the GUI
camBtn = Button(root, text=""" Activate and Record Live Feed""",
                command= camActivate, bg='palegreen', padx=30, pady=10).grid(column=0, row=1)


ExitBtn = Button(root, text='Exit Program',
                 command= root.destroy, bg='brown1', padx=30, pady=10).grid(column=0, row=3)

root.mainloop()
cv2.destroyAllWindows()
cap.release()
