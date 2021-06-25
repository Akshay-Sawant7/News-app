from django.shortcuts import render
from newsapi import NewsApiClient
from django.http import HttpResponse

def Index(request):
    newsapi = NewsApiClient(api_key="0e002ad0368f4841aaab22527dde796f")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")
    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

        mylist = zip(news, desc, img)
        return render(request, 'index.html', context={"mylist":mylist})


def bbc(request):
    newsapi = NewsApiClient(api_key="0e002ad0368f4841aaab22527dde796f")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")
    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

        mylist = zip(news, desc, img)
        return render(request, 'bbc.html', context={"mylist":mylist})



























































