import json
import random
from os.path import join
from fastapi import APIRouter

# Router
QuestionsRouter = APIRouter()
     
# FILES PATHS
questionsFilesRoot = join('whatToSay','Questions')

happyFile = join(questionsFilesRoot, 'happy.json')
sadFile = join(questionsFilesRoot, 'sad.json')
angryFile = join(questionsFilesRoot, 'anger.json')
afraidFile = join(questionsFilesRoot, 'fear.json')
disgustedFile = join(questionsFilesRoot, 'disgust.json')
generalFile = join(questionsFilesRoot, 'general.json')

greetingsFilesRoot = join('whatToSay','Greetings')

greetingFile = join(greetingsFilesRoot, 'greetings.json')

def generateSomtingToSay(dir):
    with open (dir) as file :
        data = json.load(file)
        n= random.randint(0,len(data)-1)
        return data[n]["text"]
    

@QuestionsRouter.get('/api/v1/greeting')
def greething():
    return generateSomtingToSay(greetingFile)
    
@QuestionsRouter.get('/api/v1/question/{mood}')
def generateQuestion(mood):
    if mood == 'happy':
        return generateSomtingToSay(happyFile)
    elif mood == 'sad':
        return generateSomtingToSay(sadFile)
    elif mood == 'angry':
        return generateSomtingToSay(angryFile)
    elif mood == 'afraid':
        return generateSomtingToSay(afraidFile)
    elif mood == 'disgusted':
        return generateSomtingToSay(disgustedFile)
    else:
        return generateSomtingToSay(generalFile)

