from fastapi import APIRouter
from middelware.APISMiddelware import getGenreID,getGenresName,getRandomNumber,getResponseAsJson


music = APIRouter()
BASE_URL = f"https://api.deezer.com/genre"

movie_json=getResponseAsJson(BASE_URL)


@music.get('/music/geners/list')
def get_all_music_geners():
    return getGenresName(BASE_URL,"data")

@music.get('/music/discover/with_genres/{genere}')
def get_music_by_genre(genere):
    try:
     genereid=getGenreID(genere,"data",BASE_URL)
    
     movie_json = getResponseAsJson(f"https://api.deezer.com/chart/{genereid}?&limit=50")

     randomNumber= getRandomNumber(len(movie_json["tracks"]["data"])-1)
     
     return movie_json["tracks"]["data"][randomNumber]["title"] + " by " + movie_json["tracks"]["data"][randomNumber]["artist"]["name"]
  
    except:
        #we can handel this error by adding this "text-transform: capitalize;" in the css in the input filed 
        return 'Invalid catgory (Note : Please check that the first letter is capitalized)' 
