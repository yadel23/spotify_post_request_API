import requests, spotipy, json, sqlalchemy
import pandas as pd
from sqlalchemy import create_engine

def instructions():
    print(''' 
      1. Go to spotify and go to the artist of your choosing
      2. Go to the follow button under their name, click the three dots
      3. click the 'share' button and then the 'copy link to artist' button
      4. paste this as your input
      5. go to mysql to see table
      ''')


#hard coded does not need tests
def heardcoded_apiInfo():
    url = 'https://accounts.spotify.com/api/token' 
    client_id = 'cc9846731cd64c33befaa1beb31f4886' 
    client_secret = 'a0c7aaad594a4406b6563b9b2a2e28b7'
    response = requests.post(url, {
      'grant_type': 'client_credentials',
      'client_id': client_id,
      'client_secret': client_secret,
    })
    return response


# auth_response_data = response.json()
# access_token = auth_response_data['access_token']
# headers = {
#     'Authorization': 'Bearer {token}'.format(token=access_token)
# }

#base_url = 'https://api.spotify.com/v1/'

#Test 3. test to handle if the input is correct
def user_inputLink():
    user_artistLink = input('Please enter link here \n')
    artist_id = user_artistLink.split('artist/')
    return artist_id[-1]


#Test 1. make test to see vaild connection to api
#Test 2. make test to see if json output is expected

def get_json(special_link, response):
    auth_response_data = response.json()
    access_token = auth_response_data['access_token']
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    
    r = requests.get('https://api.spotify.com/v1/' + 'artists/' + special_link, headers=headers)
    request_jsonformat = r.json()
#     print(request_jsonformat)
#     print('\n\n\n\n\n\n\n')
    return request_jsonformat

def create_dic(request_jsonformat):
    artist_dic = {}
    for key, value in request_jsonformat.items():
      if key == 'name' or key == 'popularity' or key == 'genres':
         artist_dic[key] = value
#     print(artist_dic)
#     print('\n\n\n\n\n')
    return artist_dic

def build_dataframe(artist_dic):
    col_names = ['name', 'popularity', 'genres']
    df = pd.DataFrame(columns = col_names)
    df.loc[len(df.index)] = [artist_dic['name'], artist_dic['popularity'], str(artist_dic['genres'])]
#     print(df)
#     print('\n\n build_dataframe working \n\n\n\n')
    return df
  
def set_dataframe(df):
    engine = create_engine('mysql://root:codio@localhost/artists')
    df.to_sql('artists_data', con=engine, if_exists = 'append', index=True)

# os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '+database_name+';"')
# #create database if it does not exist
# os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '+database_name+';"')
# os.system("mysql -u root -pcodio "+database_name+" < " + filename)

def main():
    instructions()
    special_artistId = user_inputLink()
    response = heardcoded_apiInfo()
    json_format = get_json(special_artistId, response)
    dic = create_dic(json_format)
    data_frame = build_dataframe(dic)
    set_dataframe(data_frame)    
    
# if __name__ == "__main__":
#     main()