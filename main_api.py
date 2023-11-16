
from spotify_api import *

if __name__ == '__main__':
    
    # get token to access public data

    access_token = get_access_token()
    headers = {
    'Authorization': 'Bearer {}'.format(access_token)
    }

    # search for an album

    results = search('album','play', headers)
    print('Search results:')
    print('-------------------------------------------------------')
    albums = results['albums']['items']
    for a in albums:
        print('%s by %s' % (a['name'], a['artists'][0]['name']))
    print()
    print()

    album_id = albums[0]['id']
    artist_id = albums[0]['artists'][0]['id']

    # more info about each track of the first album found

    print('Tracks of album %s' % albums[0]['name'])
    print('-------------------------------------------------------')
    result = get_album_tracks(album_id, headers)
    for track in result['items']:
        print (track['name'])
    print()
    print()

    # more information about the artist: genre, total number of followers and index of popularity

    print('Author of album %s is %s' % (albums[0]['name'], albums[0]['artists'][0]['name']))
    print('-------------------------------------------------------')
    results = get_artist(artist_id, headers)
    print('genres : %s' % ', '.join(results['genres']))
    print('total number of followers : %s' % results['followers']['total'])
    print('index of popularity : %s out of 100' % results['popularity'])
    print()
    print()


    
