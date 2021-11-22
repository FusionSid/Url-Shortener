import requests

data = {'url':'microsoft.com'}
url = "https://url-shortener.fusionsid.repl.co/api/"
response = requests.post(url, data=data)
url = response.content.decode()
print(url)