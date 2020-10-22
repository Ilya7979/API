#025fc616141c0bf373519fa68c40dd73
#58d2f013c104bd5ae4a9b9afadd94069
from pprint import pprint
import requests
url = "http://api.openweathermap.org/data/2.5/weather"
appid = "025fc616141c0bf373519fa68c40dd73"
params = {'q': 'Tokio',
          'appid' : appid}
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36"    }
response = requests.get(url,headers = headers, params = params)

j_data = response.json()
#print(response)
#pprint(j_data)
pprint(f"В городе {j_data['name']} температура {j_data['main'] ['temp'] - 273.15} градусов")
