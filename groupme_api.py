import requests
from config import ACCESS_TOKEN

def get_groups():
    url = f'https://api.groupme.com/v3/groups?token={ACCESS_TOKEN}'
    response = requests.get(url)
    return response.json()['response']

def get_member_ids(group_id, user_name_part=None):
    url = f'https://api.groupme.com/v3/groups/{group_id}?token={ACCESS_TOKEN}'
    response = requests.get(url)
    members = response.json()['response']['members']
    if user_name_part:
        return [
            {'id': member['id'], 'nickname': member['nickname']}
            for member in members if user_name_part.lower() in member['nickname'].lower()
        ]
    else:
        return [{'id': member['id'], 'nickname': member['nickname']} for member in members]
