from dotenv import load_dotenv
import os
import base64
from requests import post, get 
import json

load_dotenv()

client_id= os.getenv("CLIENT_ID")
client_secret= os.getenv("CLIENT_SECRET")

def getToken():
    authString = client_id + ":" + client_secret
    authBytes = authString.encode("utf-8")
    authBase64 = str(base64.b64encode(authBytes),"utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " +authBase64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    jsonResult = json.loads(result.content)
    token = jsonResult["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_in_genre(token, genreName): #return track name and artist
    url = "https://api.spotify.com/v1/recommendations"
    headers = get_auth_header(token)
    query= f"?limit=3&seed_genres={genreName}"

    queryURL = url + query
    result = get(queryURL, headers=headers)
    jsonResult = json.loads(result.content)["tracks"]
    if len(jsonResult)==0:
        print("Could not find a song")
        return None
    return jsonResult

def recommendTrack():
    token = getToken()
    reccTrack = search_in_genre(token, "jazz%2Chiphop")
    returnList = []
    print(len(reccTrack))
    for i in range(0,len(reccTrack)):
        urlImg = reccTrack[i]["album"]['images'][0]['url']
        artist = reccTrack[i]["album"]['artists'][0]['name']
        #print(artist +": " + reccTrack[i]["name"], urlImg)
        tracklist=[artist, reccTrack[i]["name"], urlImg]
        returnList.append(tracklist)
    return returnList

