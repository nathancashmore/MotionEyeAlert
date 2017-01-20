# MotionEyeAlert
Scripts to provide notifications when MotionEye spots activity.
Integration with Slack for the messaging and Online-Convert.com for conversion of AVI to MP4

# Installation

* ssh to your raspberry pi which has MotionEye running on it.
* clone this project (e.g. into directory /home/pi)

* Open the preferences section for your camera in MotionEye.
* Go down to Motion Notifications.
* Toggle 'Run A Command' to ON
* Enter the following command:

/home/pi/MotionEyeAlert/alert.sh BirdCam 1

Where:
BirdCam - is the Camera Name
1 - is the Camera ID

# Configuration

All the variables can be found in the projects config.py e.g.
~/MotionEyeAlert/motion_eye_alert/config.py

# Testing
nosetests
