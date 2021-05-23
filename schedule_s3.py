from apscheduler.schedulers.blocking import BlockingScheduler
from connect_s3 import sync_to_s3

target_dir = "./logs/"

scheduler = BlockingScheduler()
scheduler.add_job(sync_to_s3, 'interval', minutes=1)
scheduler.start()