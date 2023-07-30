from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('Believer Imagine Dragons', limit = 1)
last_link = videosSearch.result()['result'][-1]['link']
print(last_link)