import requests

def fetch_lyrics(artists, title):
    """
    Get lyrics from Seeds Lyrics API. Returns empty string if song not found
    """
    url = f'https://lyrics.lewagon.ai/search?artist={artists}&title={title}'
    try:
        response = requests.get(url)
        return response.json()["lyrics"]
    except:
        return ''
