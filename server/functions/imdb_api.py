import requests,json

def api_json(movie):
    response = requests.get("http://www.omdbapi.com/?t="+movie+"&apikey=dbb7f102")
    data = response.json()
    if (data["Response"] == "True") :
        new_json = json.dumps({
            "name": data['Title'],
            "rating": data['imdbRating'],
            "poster": data['Poster']
        })
    else:
        new_json = json.dumps({
            "name": movie,
            "rating": "null",
            "poster": "https://cdn.browshot.com/static/images/not-found.png"
        })
    return json.loads(new_json)
