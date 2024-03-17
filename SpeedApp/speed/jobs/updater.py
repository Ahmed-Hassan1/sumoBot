from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import *

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job_1,trigger='cron',minute='*/5')
    scheduler.start()