import schedule
import random
import time
import logging
from removal import remove_member

def schedule_removals(group_id, user_id, user_name):
    schedule.clear()
    for _ in range(2):
        hour, minute = random.randint(6, 17), random.randint(0, 59)  # 6 AM to 5 PM
        schedule_time = f"{hour:02d}:{minute:02d}"
        schedule.every().day.at(schedule_time).do(remove_member, group_id=group_id, user_id=user_id, user_name=user_name)
        logging.info(f"Scheduled removal at {schedule_time}")

def run_scheduler(group_id, user_id, user_name):
    schedule_removals(group_id, user_id, user_name)
    while True:
        schedule.run_pending()
        time.sleep(60)
        if not schedule.get_jobs():  # If all jobs have run
            schedule_removals(group_id, user_id, user_name)
