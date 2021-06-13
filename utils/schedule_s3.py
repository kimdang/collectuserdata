from apscheduler.schedulers.blocking import BlockingScheduler
from connect_s3 import sync_to_s3
import datetime

now = datetime.datetime.now()

scheduler = BlockingScheduler()
## call function sync_to_s3 everyday at 21:30, environment's default timezone
scheduler.add_job(sync_to_s3, trigger='cron', hour='21', minute='30')
print(f"Schedule program starts at {now}.")
scheduler.start()