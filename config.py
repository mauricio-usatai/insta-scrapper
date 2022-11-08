import os

USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
TARGET_PROFILE_ID = int(os.environ.get('TARGET_PROFILE_ID'))
# Monitoring config
APP_NAME = os.environ.get('APP_NAME')
MACHINE_NAME = os.environ.get('MACHINE_NAME')
DB_ACCESS_KEY_ID = os.environ.get('DB_ACCESS_KEY_ID')
DB_SECRET_ACCESS_KEY = os.environ.get('DB_SECRET_ACCESS_KEY')
FREQUENCY = os.environ.get('FREQUENCY')