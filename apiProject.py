import requests
import spotipy

url = 'https://accounts.spotify.com/api/token'
client_id = 'cc9846731cd64c33befaa1beb31f4886'
client_secret = 'a0c7aaad594a4406b6563b9b2a2e28b7'
response = requests.post(url, {
  'grant_type': 'client_credentials',
  'client_id': client_id,
  'client_secret': client_secret,
})


print(response.status_code)
print(response.json())
