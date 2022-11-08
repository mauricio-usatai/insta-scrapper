import time
import json
import schedule
import instaloader
from datetime import datetime

from config import (
  USERNAME, 
  PASSWORD,
  TARGET_PROFILE_ID,
  APP_NAME,
  DB_ACCESS_KEY_ID,
  DB_SECRET_ACCESS_KEY,
  MACHINE_NAME,
  FREQUENCY,
)
from monitoring.monitoring import Monitoring
from monitoring.config import MonitoringConfig

def main():
  L = instaloader.Instaloader()
  L.login(USERNAME, PASSWORD)

  profile = instaloader.Profile.from_id(L.context, TARGET_PROFILE_ID)
  followers = profile.get_followers()
  followees = profile.get_followees()

  followers_info = []
  followees_info = []

  for follower, followee in zip(followers, followees):
    followers_info.append({
      'username': follower.username,
      'fullname': follower.full_name
    })
    followees_info.append({
      'username': followee.username,
      'fullname': followee.full_name
    })
  
  with open(f'/app/files/followers-{datetime.now().strftime("%d-%m-%y")}.json', 'w') as fp:
    fp.write(json.dumps(followers_info, indent=2, ensure_ascii=False))

  with open(f'/app/files/followees-{datetime.now().strftime("%d-%m-%y")}.json', 'w') as fp:
    fp.write(json.dumps(followees_info, indent=2, ensure_ascii=False))

  try:
    _monitoring.send_keepalive()
  except Exception:
    pass

if __name__ == '__main__':
  monitoring_config = MonitoringConfig(
    _type='passive',
    name=APP_NAME,
    machine=MACHINE_NAME,
    monitoring_agent_endpoint='http://monitoring-agent:8084',
    db_access_key_id=DB_ACCESS_KEY_ID,
    db_secret_access_key=DB_SECRET_ACCESS_KEY,
    frequency=FREQUENCY,
  )
  _monitoring = Monitoring(monitoring_config)
  _monitoring.register('passive')

  main(_monitoring)

  schedule.every().day.at('23:00').do(lambda: main(_monitoring))
  while True:
    schedule.run_pending()
    time.sleep(1)