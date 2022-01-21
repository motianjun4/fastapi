from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer():
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
    
    def score(self, text:str):
        return self.analyzer.polarity_scores(text)

analyzer = SentimentAnalyzer()

if __name__ == '__main__':
    print(analyzer.score("This is not so bad."))