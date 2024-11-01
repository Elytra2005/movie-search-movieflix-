from flask import Flask, render_template, request # type: ignore
import requests # type: ignore 

app = Flask(__name__)


# home page decorator
@app.route("/", methods=["GET", "POST"])
def search():
    return render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
      read = open("stuff.txt", "r").read() 
      searchData = str(request.form.get("search-field")) #gets the movie name you are searching for 
      url = "http://www.omdbapi.com/?s=" + searchData + "&apikey=" + read #sturctures the url  
      r = requests.get(url)
      searchResults = r.json()  
      # if searchData not in searchResults["Search"]:
      #    return "Sorry this movie does not exist!"
    else:
      print("Error")

    return render_template("result.html", searchName = searchData, searchResults = searchResults)  
 
@app.route("/movie", methods=["GET", "POST"])
def moveiResults():
    read = open("stuff.txt", "r").read() 
    searchData = request.args.get("movie_title") #gets the movie name you are searching for 
    url = "http://www.omdbapi.com/?t=" + searchData + "&plot=full" + "&apikey=" + read 
    r = requests.get(url)
    searchResults = r.json()
    
    # variables to put into the html
    movieData = searchResults["Title"]
    Genre = searchResults["Genre"]
    Released = searchResults["Year"]
    Rated = searchResults["Rated"]
    imdb = searchResults["imdbRating"]
    imdbID = searchResults.get("imdbID", "no id found")
    Writer = searchResults["Writer"]
    Actors = searchResults["Actors"]
    Poster = searchResults["Poster"]
    Plot = searchResults["Plot"]
    
    return render_template("movie.html",  searchResults = searchResults, movieData=movieData, Genre=Genre, Released=Released, Rated=Rated, imdb=imdb, Writer=Writer, Actors=Actors, Poster=Poster, imdbID=imdbID, Plot=Plot)









if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")


#error log
#so there were alot of errors last night and one of them was the fact that search data was refrenced before assignment and also that the form is returning None for no reason. sigh..