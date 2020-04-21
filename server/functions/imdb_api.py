import requests,json

def api_json(movie):
    response = requests.get("http://www.omdbapi.com/?t="+movie+"&apikey=dbb7f102")
    data = response.json()
    new_json = json.dumps({
        'name': data['Title'],
        'rating': data['imdbRating'],
        'poster': data['Poster']
    })
    return json.loads(new_json)
