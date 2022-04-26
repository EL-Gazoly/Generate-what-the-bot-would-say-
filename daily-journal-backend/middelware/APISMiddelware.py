import requests
import json
import random
def getGenresList(link):
    movie_response = requests.get(link)
    movie_json = json.loads(movie_response.text)
    return movie_json


def getGenreID(genere,nameOfList,link):
    movie_json=getGenresList(link)
    for i in range(0,len(movie_json[nameOfList])):
       if movie_json[nameOfList][i]["name"]==genere:
        genereid=movie_json[nameOfList][i]["id"]
        return genereid
    
    
def getRandomNumber(boundry):
    n= random.randint(1,boundry)
    return n 
    

def getGenresName(link,nameOfList):
    movie_json=getGenresList(link)
    db =[]
    for i in range(0,len(movie_json[nameOfList])):
        db.append(movie_json[nameOfList][i]["name"])
    return db


def getResponseAsJson(linkofList):
     movie_response = requests.get(linkofList)
     movie_json = json.loads(movie_response.text)
     return movie_json