import json
import random
from os.path import join
from nltk.sentiment import SentimentIntensityAnalyzer

from fastapi import APIRouter

ResponsesRouter = APIRouter()
sia = SentimentIntensityAnalyzer()

# FILES PATHS
questionsFilesRoot = join('whatToSay','Questions')

happyFile = join(questionsFilesRoot, 'happy.json')
sadFile = join(questionsFilesRoot, 'sad.json')
angryFile = join(questionsFilesRoot, 'anger.json')
afraidFile = join(questionsFilesRoot, 'fear.json')
disgustedFile = join(questionsFilesRoot, 'disgust.json')
generalFile = join(questionsFilesRoot, 'general.json')


@ResponsesRouter.get('/api/v1/response/{msg}')
def generateResponse(msg):
    """
        Generate bot responses by analyzing the user msg.
    """
    scores = sia.polarity_scores(msg)
    sentiment, _ = getSentimentWithHighestScore(scores)

    if sentiment == 'pos':
        # return a positive sentence
        return {'pos':scores}
    elif sentiment == 'neg':
        # return a sad response 
        return {'neg':scores}
    else:
        # return a neutral thing
        return {'neu':scores}


def generateSomtingToSay(dir):
    with open (dir) as file :
        data = json.load(file)
        n = random.randint(0,len(data)-1)
        return data[n]["text"]
    
def getSentimentWithHighestScore(scores):

    sentiment = 'pos' if scores['pos'] > scores['neg'] else 'neg'
    sentiment = 'neu' if scores['neu'] > scores[sentiment] else sentiment
    
    return sentiment, scores[sentiment]