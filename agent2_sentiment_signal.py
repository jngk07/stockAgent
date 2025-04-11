
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_news(news_articles):
    analyzer = SentimentIntensityAnalyzer()
    compound_scores = []

    for article in news_articles:
        score = analyzer.polarity_scores(article)['compound']
        compound_scores.append(score)

    avg_score = sum(compound_scores) / len(compound_scores)
    
    if avg_score > 0.3:
        return "BUY", avg_score
    elif avg_score < -0.3:
        return "SELL", avg_score
    else:
        return "HOLD", avg_score

# Test
if __name__ == "__main__":
    sample_news = [
        "Tesla's stock surges after positive delivery numbers.",
        "Analysts remain bullish on Tesla’s growth in 2025."
    ]
    decision, score = analyze_news(sample_news)
    print(f"Sentiment Score: {score:.2f} → Decision: {decision}")
