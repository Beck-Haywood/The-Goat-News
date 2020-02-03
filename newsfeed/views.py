from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient
import requests
import json
import pandas

# Create your views here.
def newsfeed(request):
    template_name = 'newsfeed.html'
    headers = {'Authorization': '1757fcbd46b14cdea7eda377d1906a60'}
    top_headlines_url = 'https://newsapi.org/v2/top-headlines'
    everything_news_url = 'https://newsapi.org/v2/everything'
    sources_url = 'https://newsapi.org/v2/sources'
    headlines_payload = {'category': 'business', 'country': 'us'}
    everything_payload = {'q': 'finance', 'language': 'en', 'sortBy': 'popularity'}
    sources_payload = {'category': 'general', 'language': 'en', 'country': 'us'}

    #response = requests.get(url=top_headlines_url, headers=headers, params=headlines_payload)

    response = requests.get(url=everything_news_url, headers=headers, params=everything_payload)

    response_data = response.json()



    print(response_data['status'])
    print(response_data['totalResults'])
    article1 = response_data['articles']
    #print(article1)
    print('-------------------------------')
    print(article1[1])
    print(article1[1]['source']['name'])
    source = article1[1]['source']['name']
    author = article1[1]['author']
    title = article1[1]['title']
    url = article1[1]['url']
    content = article1[1]['content']
    image = article1[1]['urlToImage']
    description = article1[1]['description']




    pretty_json_output = json.dumps(response.json(), indent=4)
    #print(pretty_json_output)
    response_json_string = json.dumps(response.json())
    response_dict = json.loads(response_json_string)


    articles_list = response_dict['articles']

    df = pandas.read_json(json.dumps(articles_list))
    context = {'source': source, 'title': title, 'author': author, 'url': url, 'content': content, 'image': image, 'description': description}




 

    return render(request, template_name, context)
