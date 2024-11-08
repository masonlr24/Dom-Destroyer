import requests
import logging
from config import ACCESS_TOKEN

# Configure logging
logging.basicConfig(filename='groupme_removal.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Counter for removals
removal_count = 0

def remove_member(group_id, user_id, user_name):
    global removal_count
    url = f'https://api.groupme.com/v3/groups/{group_id}/members/{user_id}/remove?token={ACCESS_TOKEN}'
    response = requests.post(url)
    if response.status_code == 200:
        removal_count += 1
        logging.info(f"Successfully removed member: {user_name} (Count: {removal_count})")
    else:
        logging.error(f"Failed to remove member: {response.status_code} - {response.text}")

def nuke_group(group_id, members):
    for member in members:
        remove_member(group_id, member['id'], member['nickname'])
