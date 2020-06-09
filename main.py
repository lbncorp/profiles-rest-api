import requests

response = requests.get('https://https://httpbin.org/ip')

print('Your IP is {0}' .format(response.json()['origin']))

