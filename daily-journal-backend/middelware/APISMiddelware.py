import requests
import json
import random


def getGenreID(genere,nameOfList,link):
    movie_json=getResponseAsJson(link)
    for i in range(0,len(movie_json[nameOfList])):
       if movie_json[nameOfList][i]["name"]==genere:
        genereid=movie_json[nameOfList][i]["id"]
        return genereid
    
    
def getRandomNumber(boundry):
    n= random.randint(1,boundry)
    return n 
    

def getGenresName(link,nameOfList):
    movie_json=getResponseAsJson(link)
    db =[]
    for i in range(0,len(movie_json[nameOfList])):
        db.append(movie_json[nameOfList][i]["name"])
    return db


def getResponseAsJson(linkofList):
     movie_response = requests.get(linkofList)
     movie_json = json.loads(movie_response.text)
     return movie_json