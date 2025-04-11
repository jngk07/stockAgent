
from newsapi import NewsApiClient

#def get_news(company, api_key):
#    newsapi = NewsApiClient(api_key=api_key)
#    articles = newsapi.get_everything(q=company, language='en', sort_by='relevancy', page_size=5)
#    news = [article['title'] + " - " + article['description'] for article in articles['articles']]
#    return news

def get_news(company, api_key=None):
  # Custom test news for demo purposes
    return [
        f"US president removed Tariffs and annouced FED rate cuts"
        f"{company} stock explodes after incredible earnings blowout and very strong growth! 🚀",
        f"Top analysts overwhelmingly upgrade {company}, calling it a must-buy!",
        f"{company} revolutionizes the market with mind-blowing AI tech. Investors thrilled!"
    ]

# Test
if __name__ == "__main__":
    company = "Tesla"
    news = get_news(company, api_key="YOUR_NEWS_API_KEY")
    for i, article in enumerate(news, 1):
        print(f"{i}. {article}\n")
