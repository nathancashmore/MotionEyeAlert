# MotionEyeAlert
Scripts to provide notifications when MotionEye spots activity.
Integration uses:

* __Slack__ - For delivering the notifications.

# Installation

* Install MotionEye on your Raspberry Pi (https://github.com/ccrisan/motioneye/wiki/Installation)
* Clone this project into the home directory on the Pi 
* Add the following command on the MotionEye in 
_Preferences > Motion Notifications > Command_
``/home/pi/MotionEyeAlert/alert.sh 1 MyCamera``

Where:

``MyCamera`` - is the Camera Name and 
``1`` - is the Camera ID

# Configuration

Environment variables must be set for the application to run:

```
export MOTION_EYE_SERVER_URL=http://motioncam.somewhere.com
export MOTION_EYE_USER=admin
export MOTION_EYE_SIGNATURE=xxxxxxxxxxxxxxxxxx
export SLACK_WEBHOOK_URL=https://hooks.slack.com/services/XXXXXXX/XXXXXX/XXXXXXXXXX
export SLACK_CHANNEL=alert
```

##Slack
* Register on Slack on the [Create a New Team page](https://slack.com/create#email)
* Add a new webhook and channel you would like to use for notifications on the [Incoming-Webhook setup page](https://my.slack.com/services/new/incoming-webhook/)
* Put the Webhook URL and channel name in the config file.

# Testing
Run the tests using
```nosetests```
