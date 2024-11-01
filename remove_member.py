import requests
import logging
import schedule
import time
import random

# Constants
ACCESS_TOKEN = 'jB3YayE7jp5sB7uTj7EIEBybHPke69bD7LlObn0k'  # GroupMe access token
GROUP_ID = '34051141'  # Group ID
USER_ID_TO_REMOVE = '703750157'  # User ID to remove
USER_NAME_TO_REMOVE = 'Dominic Dalpoas'  # User's name to remove

# Configure logging
logging.basicConfig(filename='groupme_removal.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Counter for removals
removal_count = 0

def remove_member():
    global removal_count
    url = f'https://api.groupme.com/v3/groups/{GROUP_ID}/members/{USER_ID_TO_REMOVE}/remove?token={ACCESS_TOKEN}'
    response = requests.post(url)
    if response.status_code == 200:
        removal_count += 1
        logging.info(f"Successfully removed member: {USER_NAME_TO_REMOVE} (Count: {removal_count})")
    else:
        logging.error(f"Failed to remove member: {response.status_code} - {response.text}")

def schedule_removals():
    schedule.clear()
    for _ in range(2):
        hour, minute = random.randint(6, 17), random.randint(0, 59)  # 6 AM to 5 PM
        schedule_time = f"{hour:02d}:{minute:02d}"
        schedule.every().day.at(schedule_time).do(remove_member)
        logging.info(f"Scheduled removal at {schedule_time}")

# Initial scheduling
schedule_removals()

# Main loop
while True:
    schedule.run_pending()
    time.sleep(60)
    if not schedule.get_jobs():  # If all jobs have run
        schedule_removals()
