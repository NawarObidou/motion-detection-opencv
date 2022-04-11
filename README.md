# motion-detection-opencv
This software is a proof of concept design created for the purpose of moinotring movement within a camera's field of vision. This is achieved by using computer vision through python. 
The code will:
  Open a live camera feed, most likely being the device's default built-in camera.
  Draw squares around movement. it has been designed to ignore 'noise' from smaller movements.
  Provide a visual text alert on the screen notifying that movement has beed picked up
  Provide a visual representaion of a light turning on (green) when movement is detected, and off (red) when there is no moevement
