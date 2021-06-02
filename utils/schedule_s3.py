from apscheduler.schedulers.blocking import BlockingScheduler
from connect_s3 import sync_to_s3


scheduler = BlockingScheduler()
scheduler.add_job(sync_to_s3, 'interval', days=1)
scheduler.start()