from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import *

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job_2,'interval',seconds=2)
    scheduler.start()