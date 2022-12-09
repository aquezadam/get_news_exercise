import requests
import json


def news_fetch(query,date):
    url = f"https://newsapi.org/v2/everything?q={query}&from={date}&sortBy=publishedAt&apiKey=171592ef0ef6497ebb86a6b551a2d5b6"
    print(query, date)
    response = requests.get(url)
    print(url)
    print(json.dumps(response.json(), indent=4, separators=(". ", " = ")))
    news_dictionary_articles = response.json()["articles"][:10]
    new_list = []
    for i in news_dictionary_articles:
        del i["source"]
        new_list.append(i)
    return new_list
# print(news_fetch("tesla"))
