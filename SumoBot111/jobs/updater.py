from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import *

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job_1,'interval',seconds=2)
    scheduler.add_job(FutureIndicatorFourSupport,trigger='cron',minute='*/5')
    scheduler.start()