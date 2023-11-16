import requests
import json

SPOTIFY_BASE_URL = "https://api.spotify.com"
SPOTIFY_API_URL = "https://api.spotify.com/v1"

# 0. GET TOKEN

CLIENT = json.load(open('conf.json', 'r+'))
CLIENT_ID = CLIENT['id']
CLIENT_SECRET = CLIENT['secret']

SPOTIFY_TOKEN_URL = "{}/{}".format("https://accounts.spotify.com", 'api/token')

def get_access_token():

    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    auth_response = requests.post(SPOTIFY_TOKEN_URL, data=data)
    access_token = auth_response.json().get('access_token')

    return access_token

# 1. ALBUM

GET_ALBUM_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'albums')

def get_album(album_id, headers):
    url = "{}/{id}".format(GET_ALBUM_ENDPOINT, id=album_id)
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_several_albums(album_ids, headers):
    url = "{}/?ids={ids}".format(GET_ALBUM_ENDPOINT, ids=','.join(album_ids))
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_album_tracks(album_id, headers):
    url = "{}/{id}/tracks".format(GET_ALBUM_ENDPOINT, id=album_id)
    resp = requests.get(url, headers=headers)
    return resp.json()

# 2. ARTIST

GET_ARTIST_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'artists')

def get_artist(artist_id, headers):
    url = "{}/{id}".format(GET_ARTIST_ENDPOINT, id=artist_id)
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_several_artists(artist_ids, headers):
    url = "{}/?ids={ids}".format(GET_ARTIST_ENDPOINT, ids=','.join(artist_ids) )
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_artists_albums(artist_id, headers):
    url = "{}/{id}/albums".format(GET_ARTIST_ENDPOINT, id=artist_id)
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_artists_top_tracks(artist_id, headers):
    url = "{}/{id}/top-tracks".format(GET_ARTIST_ENDPOINT, id=artist_id)
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_artist_related_artists(artist_id, headers):
    url = "{}/{id}/related-artists".format(GET_ARTIST_ENDPOINT, id=artist_id)
    resp = requests.get(url, headers=headers)
    return resp.json()

# 3. SEARCH

SEARCH_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'search')

def search(search_type, name, headers):
    if search_type not in ['artist', 'track', 'album', 'playlist']:
        print('invalid type')
        return None
    myparams = {'type': search_type}
    myparams['q'] = name
    resp = requests.get(SEARCH_ENDPOINT, params=myparams, headers=headers)
    return resp.json()

# 4. TRACK

GET_TRACK_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'tracks')

def get_track(track_id, headers):
    url = "{}/{id}".format(GET_TRACK_ENDPOINT, id=track_id)
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_several_tracks(track_ids, headers):
    url = "{}/?ids={ids}".format(GET_TRACK_ENDPOINT, ids=','.join(track_ids))
    resp = requests.get(url, headers=headers)
    return resp.json()

# # 5. USER

# GET_USER_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'users')

# def get_user(user_id, headers):
#     url = "{}/{id}".format(GET_USER_ENDPOINT, id=user_id)
#     resp = requests.get(url, headers=headers)
#     return resp.json()

# # 6. USER RELATED REQUESTS  

# # spotify endpoints
# USER_PROFILE_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'me')
# USER_PLAYLISTS_ENDPOINT = "{}/{}".format(USER_PROFILE_ENDPOINT, 'playlists')
# USER_TOP_ARTISTS_AND_TRACKS_ENDPOINT = "{}/{}".format(
#     USER_PROFILE_ENDPOINT, 'top')  # /<type>
# USER_RECENTLY_PLAYED_ENDPOINT = "{}/{}/{}".format(USER_PROFILE_ENDPOINT,
#                                                   'player', 'recently-played')
# BROWSE_FEATURED_PLAYLISTS = "{}/{}/{}".format(SPOTIFY_API_URL, 'browse',
#                                               'featured-playlists')

# def get_users_profile(headers):
#     url = USER_PROFILE_ENDPOINT
#     resp = requests.get(url, headers=headers)
#     return resp.json()

# def get_users_playlists(headers):
#     url = USER_PLAYLISTS_ENDPOINT
#     resp = requests.get(url, headers=headers)
#     return resp.json()

# def get_users_top(headers, t):
#     if t not in ['artists', 'tracks']:
#         print('invalid type')
#         return None
#     url = "{}/{type}".format(USER_TOP_ARTISTS_AND_TRACKS_ENDPOINT, type=t)
#     resp = requests.get(url, headers=headers)
#     print(resp)

# def get_users_recently_played(headers):
#     url = USER_RECENTLY_PLAYED_ENDPOINT
#     resp = requests.get(url, headers=headers)
#     return resp.json()

# def get_featured_playlists(headers):
#     url = BROWSE_FEATURED_PLAYLISTS
#     resp = requests.get(url, headers=headers)
#     return resp.json()