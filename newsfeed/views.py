from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient
from newsapi import NewsApiClient 
import requests
import json
import pandas

# Create your views here.  
def index(request): 
      
    newsapi = NewsApiClient(api_key ='1757fcbd46b14cdea7eda377d1906a60') 
    top = newsapi.get_top_headlines(sources ='techcrunch') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
    mylist = zip(news, desc, img) 
  
    return render(request, 'index.html', context ={"mylist":mylist}) 
def newsfeed(request):
    template_name = 'newsfeed.html'
    number_of_articles = 3

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
    print('-------------------------------')


    dic = {}

    for i in range(number_of_articles):
        print(i)

        articles = response_data['articles']
        source = articles[i]['source']['name']
        author = articles[i]['author']
        title = articles[i]['title']
        url = articles[i]['url']
        content = articles[i]['content']
        image = articles[i]['urlToImage']
        description = articles[i]['description']
        #dic[i] = [source, author, title, url, content, image, description]
        dic[str(i)] = {'source': source, 'author': author, 'title': title, 'url': url, 'content': content, 'image': image, 'description': description}
    # print(dic)

    #print(article1)
    # print('-------------------------------')
    # print(article1[1])
    # print(article1[1]['source']['name'])
    # source = article1[1]['source']['name']
    # author = article1[1]['author']
    # title = article1[1]['title']
    # url = article1[1]['url']
    # content = article1[1]['content']
    # image = article1[1]['urlToImage']
    # description = article1[1]['description']




    #pretty_json_output = json.dumps(response.json(), indent=4)
    #print(pretty_json_output)
    #response_json_string = json.dumps(response.json())
    #response_dict = json.loads(response_json_string)


    #articles_list = response_dict['articles']

    #df = pandas.read_json(json.dumps(articles_list))
    #context = {'source': source, 'title': title, 'author': author, 'url': url, 'content': content, 'image': image, 'description': description}
    #context = {'dic': dic, 'number_of_articles': number_of_articles}
    context = dic
    print(context)
   

    return render(request, template_name, {"context": context})
