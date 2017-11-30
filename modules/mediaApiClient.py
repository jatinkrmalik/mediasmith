import requests
api_key = "b24f4d67b594162aead6de65f7c96066"

class MediaInfo:
    def __init__(self):
        self.key = api_key
    
    ## SEARCH METHODS
    def search_multi(self, mediaName):
        url = "https://api.themoviedb.org/3/search/multi"
        response = requests.request("GET", url + "?api_key=" + api_key + "&language=en-US&query=" + mediaName + "&page=1&include_adult=false")
        return response.text

    def search_movie(self, movieName):
        url = "https://api.themoviedb.org/3/search/movie"
        response = requests.request("GET", url + "?api_key=" + api_key + "&language=en-US&query=" + movieName + "&page=1&include_adult=false")
        return response.text

    def search_tv(self, tvShowName):
        url = "https://api.themoviedb.org/3/search/tv"
        response = requests.request("GET", url + "?api_key=" + api_key + "&language=en-US&query=" + tvShowName + "&page=1&include_adult=false")
        return response.text
    
    def search_collections(self, collectionName):
        url = "https://api.themoviedb.org/3/search/collection"
        response = requests.request("GET", url + "?api_key=" + api_key + "&language=en-US&query=" + movieName + "&page=1")
        return response.text

    ## GET METHODS

