import json
import random
from fastapi import APIRouter

generate = APIRouter()

def generateSomtingToSay(dir):
    with open (dir) as file :
        data = json.load(file)
        n= random.randint(0,len(data)-1)
        return data[n]["text"]
    

@generate.get('/greetings')
def greething():
    return generateSomtingToSay('./whatToSay/greetings.json')
    
    
@generate.get('/mood/happy')
def Happy():
    return generateSomtingToSay('./whatToSay/happy.json')
    
@generate.get('/mood/sad')
def sad():
    return generateSomtingToSay('./whatToSay/sad.json')
    
    
@generate.get('/mood/anger')
def anger():
    return generateSomtingToSay('./whatToSay/anger.json')
    
@generate.get('/mood/fear')
def fear():
    return generateSomtingToSay('./whatToSay/fear.json')
    
@generate.get('/mood/disgust')
def disgust():
    return generateSomtingToSay('./whatToSay/disgust.json')