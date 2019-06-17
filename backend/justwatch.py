import urllib, json
from urllib import request
from info import Info

def fetchMedia():    
    url_base = 'https://apis.justwatch.com/content/titles/en_IN/popular?body=%7B%22content_types%22:%5B%22show%22,%22movie%22%5D,%22page%22:1,%22page_size%22:7,%22query%22:%22'

    query = "santa-clarita's-diet%22%7D";

    url = url_base+query;

    response = urllib.request.urlopen(url);
    data = json.loads(response.read())

    mediaInfo = data['items'][0]

    information = Info()
    information.id = mediaInfo['id']
    information.title = mediaInfo['title']
    information.type = mediaInfo['object_type']
    information.year = mediaInfo['original_release_year']
    url_path = mediaInfo['full_path'].split("/")
    url_path = url_path[len(url_path)-1]
    photo_url = "https://images.justwatch.com"+mediaInfo['poster'].replace("{profile}","s592/"+url_path)
    information.photo = photo_url
    information.description = mediaInfo['short_description']

    offer_list = []

    droid = "deeplink_android"
    ios = "deeplink_ios"
    web = "standard_web"

    for offer in mediaInfo['offers']:
        urls = offer["urls"]
        web_url = urls['standard_web']
        if("primevideo" in web_url):
            information.amazon_android_link =urls[droid]
            information.amazon_ios_link =urls[ios]
            information.amazon_web_link=urls[web]
        elif("hotstar" in web_url):
            information.hotstar_android_link=urls[droid]
            information.hotstar_ios_link=urls[ios]
            information.hotstar_web_link=urls[web]
        elif("hulu" in web_url):
            information.hulu_android_link=urls[droid]
            information.hulu_ios_link=urls[ios]
            information.hulu_web_link=urls[web]
        elif("netflix" in web_url):
            information.amazon_android_link=urls[droid]
            information.netflix_ios_link=urls[ios]
            information.netflix_web_link=urls[web]
    print(information)
    return information

fetchMedia()