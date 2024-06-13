import json
import requests

class read_likes:
    def __init__(self):
        self.read_config()
        self.get_raw_like_json()
        self.save_json()
        self.process_json()

    def read_config(self):
        # Open config file
        with open('config.json', 'r') as f:
            # Load as json
            config = json.load(f)

            # Set keys
            self.Bearer=config['request_data']['Bearer']
            self.Auth_token=config['request_data']['auth_token']
            self.ct0=config['request_data']['ct0']
            self.Count=config['config']['count']
            self.Json_file=config['config']['json_file']
            self.Terget_user_id=config['user_data']['user_id']
            self.Terget_screen_name=config['user_data']['screen_name']

            # Set headers
            self.headers = {
                'authorization': 'Bearer {}'.format(self.Bearer),
                'content-type': 'application/json',
                'cookie': 'auth_token={}; ct0={};'.format(self.Auth_token, self.ct0),
                'x-csrf-token': '{}'.format(self.ct0)
            }
            
            # If Terget_screen_name is not empty, overwrite Terget_user_id
            if self.Terget_screen_name != "":
                self.get_user_id()
    
    def get_user_id(self):
        # Set url
        url = 'https://api.x.com/1.1/users/show.json?screen_name={}'.format(self.Terget_screen_name)
        
        # Send request
        response = requests.get(url, headers=self.headers)

        # Overwrite Terget_user_id
        self.Terget_user_id = response.json().get('id')
        print("Terget user_id overwritten to {}".format(self.Terget_user_id))

    def get_raw_like_json(self):
        # Set url
        url = 'https://api.x.com/1.1/favorites/list.json?count={}&user_id={}'.format(self.Count, self.Terget_user_id)

        # Send request
        response = requests.get(url, headers=self.headers)

        # Set returned raw json to variable
        self.raw_json = response.json()
    
    def save_json(self):
        with open(self.Json_file, 'w') as f:
            json.dump(self.raw_json, f, indent=4)

    def process_json(self):
        
        # data = json.load(open(self.Json_file, 'r'))
        data = self.raw_json

        for item in data:
            print('created_at  : ', item.get('created_at'))
            print('text        : ', item.get('text').replace("\n",""))

            entities = item.get('entities', {})
            media = entities.get('media', [{}])[0]
            media_url = media.get('media_url')

            if media_url:
                print('media_url   : ', media_url)
            else:
                pass

            print('\n')
            
if __name__ == "__main__":
    _ = read_likes()