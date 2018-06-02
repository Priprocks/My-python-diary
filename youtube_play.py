# Libraries:------------------------
import webbrowser
import requests
from bs4 import BeautifulSoup
# ----------------------------------

# Getting the query
query = input("Enter query:").replace(' ','+')

# Fetching the query page that needs to be parsed
page = requests.get('https://www.youtube.com/results?search_query='+query).text
soup = BeautifulSoup(page, 'html5lib')

# Getting the first video Link
video = soup.findAll('a',class_='yt-uix-tile-link')
link = 'https://www.youtube.com'+video[0]['href']
print('Opening up {}'.format(video[0].text))

# Opening the video in the webbrowser
webbrowser.open(link)
