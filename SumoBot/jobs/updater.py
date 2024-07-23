from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import *

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job_1,'interval',seconds=2)
    scheduler.start()