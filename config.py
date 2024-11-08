import requests

# Function to read the access token from the file
def get_access_token():
    with open('accesstoken.txt', 'r') as file:
        return file.read().strip()

# Constants
ACCESS_TOKEN = get_access_token()  # GroupMe access token
