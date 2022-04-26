from fastapi import APIRouter
from config.API_KEYS import MOVIE_API_KEY
from middelware.APISMiddelware import getRandomNumber,getGenreID,getGenresName,getResponseAsJson


RecommendationsRouter = APIRouter()

movie_api_key = '52d166f890a90c5a5658604fb8750ed7' #insert your api key here 

Movies_API_BASE_URL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={movie_api_key}"

movie_json=getResponseAsJson(Movies_API_BASE_URL)

@RecommendationsRouter.get('/api/v1/recommendations/movies')
def get_all_movies_geners():
    
    return getGenresName(Movies_API_BASE_URL,"genres")


@RecommendationsRouter.get('/api/v1/recommendations/movies/{genere}')
def get_movies_by_genre(genere):
    try:
     genereid=getGenreID(genere,"genres",Movies_API_BASE_URL)
     
     randomNumber= getRandomNumber(7)
 
     movie_json = getResponseAsJson(f"https://api.themoviedb.org/3/discover/movie?api_key={movie_api_key}&sort_by=popularity.desc&with_genres={genereid}&page={randomNumber}&language=en-US&include_adult=false")
     
     randomNumber= getRandomNumber(len(movie_json["results"])-1)
     movie = {  'title' : movie_json["results"][randomNumber]["original_title"],
                'release date' : movie_json["results"][randomNumber]["release_date"], 
                'rating' : str(movie_json["results"][randomNumber]["vote_average"]),
                'overview' : movie_json["results"][randomNumber]["overview"]
             }
     return movie
    
    except:
        #we can handel this error by adding this "text-transform: capitalize;" in the css in the input filed 
        return 'Invalid catgory (Note : Please check that the first letter is capitalized)' 



Music_API_BASE_URL = f"https://api.deezer.com/genre"

movie_json=getResponseAsJson(Music_API_BASE_URL)


@RecommendationsRouter.get('/api/v1/recommendations/music/')
def get_all_music_geners():
    return getGenresName(Music_API_BASE_URL,"data")

@RecommendationsRouter.get('/api/v1/recommendations/music/{genere}')
def get_music_by_genre(genere):
    try:
     genereid=getGenreID(genere,"data",Music_API_BASE_URL)
    
     music_json = getResponseAsJson(f"https://api.deezer.com/chart/{genereid}?&limit=50")

     randomNumber= getRandomNumber(len(movie_json["tracks"]["data"])-1)
     music = {  'title' : music_json["tracks"]["data"][randomNumber]["title"],
                'artist' : music_json["tracks"]["data"][randomNumber]["artist"]["name"]
             }
             
     return music
    
    
    except:
        #we can handel this error by adding this "text-transform: capitalize;" in the css in the input filed 
        return 'Invalid catgory (Note : Please check that the first letter is capitalized)' 
