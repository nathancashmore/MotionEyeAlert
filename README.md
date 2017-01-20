# MotionEyeAlert
Scripts to provide notifications when MotionEye spots activity.
Integration uses:

* __Slack__ - For delivering the notifications.
* __Online-Convert.com__ - To convert the AVI files to MP4's.

# Installation

* Install MotionEye on your Raspberry Pi (https://github.com/ccrisan/motioneye/wiki/Installation)
* Clone this project into the home directory on the Pi 
* Add the following command on the MotionEye in 
_Preferences > Motion Notifications > Command_
``/home/pi/MotionEyeAlert/alert.sh BirdCam 1``

Where:
``BirdCam`` - is the Camera Name
``1`` - is the Camera ID

# Configuration

All the variables can be found in the projects config.py e.g.
~/MotionEyeAlert/motion_eye_alert/config.py

You will need an API key for Online-Convert.com and a webhook in Slack

##Online-Convert.com
* Register with [Online-Convert.com](https://www.online-convert.com/signup/free)
* Copy the API key from the [Subscription Details page](https://www.online-convert.com/subscription-details) into the config file.

##Slack
* Register on Slack on the [Create a New Team page](https://slack.com/create#email)
* Add a new webhook and channel you would like to use for notifications on the [Incoming-Webhook setup page](https://my.slack.com/services/new/incoming-webhook/)
* Put the Webhook URL and channel name in the config file.

# Testing
Run the tests using
```nosetests```
