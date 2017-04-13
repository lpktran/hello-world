import requests
from bs4 import BeautifulSoup

base_url = "http://api.genius.com/"
headers = {'Authorization': 'Bearer WxfjRpPbrOL3BR6dDMilNrBkxIDrpkzxjdmI-XGHzRQOzEcrkMRhrjKUHqUZS5Bl'}

song_title = "Lake Song"
artist_name = "The Decemberists"

def lyrics_from_song_api_path(song_api_path):
	song_id = str(song_api_path)
	song_url = base_url + 'songs/' + song_id
	response = requests.get(song_url, headers=headers)
	json = response.json()
	path = json["response"]["song"]["path"]
	page_url = "http://genius.com" + path
	page = requests.get(page_url)
	html = BeautifulSoup(page.text, "html.parser")
	#remove script tags that they put in the middle of the lyrics
	[h.extract() for h in html('script')]
	#at least Genius is nice and has a tag called 'lyrics'!
	lyrics = html.find("lyrics").get_text()
	lyrics = lyrics.replace('\n', ' ')
	return lyrics

# if __name__ == "__main__":
#   search_url = base_url + "/search"
#   data = {'q': song_title}
#   response = requests.get(search_url, data=data, headers=headers)
#   json = response.json()
#   song_info = None
#   print(response)
#   # for hit in json["response"]["hits"]:
#   #   if hit["result"]["primary_artist"]["name"] == artist_name:
#   #     song_info = hit
#   #     break
#   # if song_info:
#   #   song_api_path = song_info["result"]["api_path"]
#   #   print (lyrics_from_song_api_path(song_api_path))

def get_color_info():
	""" scrapes info on color theory from a blog post """
	color_url = "http://www.arttherapyblog.com/online/color-psychology-psychologica-effects-of-colors/#.WO_g0FMrKTf"
	response = requests.get(color_url)
	
	if response.status_code == 404:                 # page not found
		print("There was a problem with getting the page:")
		print(buzz_menu_url)
	
	data_from_url = response.text
	soup = BeautifulSoup(data_from_url, "lxml")
	return soup

def extract_colors():
	""" extract_colors takes in a beautiful soup object, soup
		and uses Beautiful Soup to extract a list of all of sentimental info of colors
		
		it returns a list of colors and its associated emotions
	"""
	soup = get_color_info()
	AllDivs = soup.body.find_all("strong")
	list_of_colors = []
	list_of_emotions = []
	for color in AllDivs: 
		Words = color.text.split()
		print(Words)
		if "Color" in Words:
			color_index = Words.index("Color")
			colorname = Words[ color_index-1 ]  # it's the one BEFORE!
			colorname = colorname.lower()         # make lower case
			list_of_colors.append( colorname )

