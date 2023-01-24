import json
import requests

def read_jsonFile(): #reading urls from file
    with open('config.json') as json_file:
      data = json.load(json_file)
      return data
  
def save_url(data): #saving response time in file
    with open('response_time.json', 'w') as file:
      json.dump(data, file, indent=2)

class ResponseTime:
    
    def get_response(self): #getting response time of all the urls present in the mentioned file
        self.data = read_jsonFile()
        for p in self.data['urls']:
            # print('url: ' + p['name'])
            r = requests.get(p['name'])
            # print(r.elapsed.total_seconds())
            p['response_time'] = r.elapsed.total_seconds()
        save_url(self.data)
        
    def multiple_response(self,no): #getting multiple response time of all the urls present in the mentioned file
        self.data = read_jsonFile()
        for p in self.data['urls']:
            p['response_time'] = []
            for i in range(no):
                r = requests.get(p['name'])
                p['response_time'].append( r.elapsed.total_seconds())
        with open('multi_response.json', 'w') as f:
           json.dump(self.data, f, indent=4)

    