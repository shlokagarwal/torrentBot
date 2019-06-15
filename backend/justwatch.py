import urllib, json
from urllib import request

url_base = 'https://apis.justwatch.com/content/titles/en_IN/popular?body=%7B%22content_types%22:%5B%22show%22,%22movie%22%5D,%22page%22:1,%22page_size%22:7,%22query%22:%22'

query = "santa-clarita's-diet%22%7D";

url = url_base+query;

response = urllib.request.urlopen(url);
data = json.loads(response.read())

print(type(data["items"]))
print(type(data["items"][0]))
print(type(data["items"][0]["offers"]))
