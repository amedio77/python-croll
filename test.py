import requests
import pymysql.cursors
from bs4 import BeautifulSoup
from collections import OrderedDict
import pandas as pd

url = 'http://www.melon.com/chart/index.htm'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

song_dict = OrderedDict()
for tr_tag in soup.select('#tb_list tr[data-song-no]'):
    song_no = tr_tag.attrs['data-song-no']
    title = tr_tag.select('a[href*=playSong]')[0].text.strip()
    artist = tr_tag.select('a[href*=goArtistDetail]')[0].text.strip()
    album = tr_tag.select('a[href*=goAlbumDetail]')[0].text.strip()

    song_dict[song_no] = {
        'title': title,
        'artist': artist,
        'album': album,
        'like': 0,
    }

conts_ids = ','.join(song_no for song_no in song_dict)

url = 'http://www.melon.com/commonlike/getSongLike.json'
params = {'contsIds': conts_ids}

like_dict = requests.get(url, params=params).json()
for row in like_dict['contsLike']:
    song_no = str(row['CONTSID'])  # int to str
    song_dict[song_no]['like'] = row['SUMMCNT']

df = pd.DataFrame(list(song_dict.values()), columns=['title', 'artist', 'album', 'like'])
print(df)






