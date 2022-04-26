from fastapi import APIRouter
from config.API_KEYS import MOVIE_API_KEY
from middelware.APISMiddelware import getGenresList,getRandomNumber,getGenreID,getGenresName,getResponseAsJson

movie = APIRouter()

movie_api_key = MOVIE_API_KEY #insert your api key here 

BASE_URL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={movie_api_key}"

movie_json=getGenresList(BASE_URL)

@movie.get('/movies/geners/list')
def get_all_movies_geners():
    
    return getGenresName(BASE_URL,"genres")


@movie.get('/movies/discover/with_genres/{genere}')
def get_movies_by_genre(genere):
    try:
     genereid=getGenreID(genere,"genres",BASE_URL)
     
     randomNumber= getRandomNumber(7)
 
     movie_json = getResponseAsJson(f"https://api.themoviedb.org/3/discover/movie?api_key={movie_api_key}&sort_by=popularity.desc&with_genres={genereid}&page={randomNumber}&language=en-US&include_adult=false")
     
     randomNumber= getRandomNumber(len(movie_json["results"])-1)
     
     return movie_json["results"][randomNumber]["original_title"] + '  release date : ' + movie_json["results"][randomNumber]["release_date"] + " vote_average : " + str(movie_json["results"][randomNumber]["vote_average"]) + " overview : " + movie_json["results"][randomNumber]["overview"] 
    
    except:
        #we can handel this error by adding this "text-transform: capitalize;" in the css in the input filed 
        return 'Invalid catgory (Note : Please check that the first letter is capitalized)' 



