import requests
import spotipy
import json

url = 'https://accounts.spotify.com/api/token' 
client_id = 'cc9846731cd64c33befaa1beb31f4886' 
client_secret = 'a0c7aaad594a4406b6563b9b2a2e28b7'
response = requests.post(url, {
  'grant_type': 'client_credentials',
  'client_id': client_id,
  'client_secret': client_secret,
})

auth_response_data = response.json()

access_token = auth_response_data['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

base_url = 'https://api.spotify.com/v1/'
track_id = '4vDBJeeQCbhP9FaPPMsYkY?si=992cc74ea4564ff6'
artist_id = '3TVXtAsR1Inumwj472S9r4?si=z1z0cXVQTtefzolOGqO6Zw&dl_branch=1'

r = requests.get(base_url + 'artists/' + artist_id, headers=headers)
request_jsonformat = r.json()

for key, value in request_jsonformat.items():
  if key == 'name' or key == 'popularity' or key == 'genres':
   print(key, ":", value)   
  