from distutils.core import setup

setup(name='MotionEyeAlert',
      version='0.1',
      py_modules=[
          'motion_eye_alert/slack_client',
          'motion_eye_alert/alert_handler'],
      )
