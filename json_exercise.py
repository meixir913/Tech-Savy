import urllib.request
import json
import pprint

APIKEY = '534fe94d3f9ac0a5e7e9228fc7fefd68'
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint.pprint(response_data)

# Can you get the current temperature in Wellesley?
#METHOD 1
print(response_data['main'])
main=response_data['main']
print(main['temp'],'is the current temperature in Wellesley')
#METHOD 2
print(response_data['main']['temp'],'is the current temperature in Wellesley')