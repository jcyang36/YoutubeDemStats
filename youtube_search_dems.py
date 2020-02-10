import pandas as pd
import urllib.request
import json

#api key
key = "key=YOURKEYHERE"

#search api and params
youtube_search = "https://www.googleapis.com/youtube/v3/search?"
part_search = "part=snippet"
order_views = "order=viewCount"
max_results = "maxResults=50"
date_filter = "publishedAfter=2019-01-01T00:00:00Z"

#list of candidates
candidates = ['Joe+Biden','Cory+Booker','Pete+Buttigieg','Tulsi+Gabbard',
                'Kamala+Harris','Amy+Klobuchar','Bernie+Sanders','Tom+Steyer',
                'Elizabeth+Warren','Andrew+Yang']

#set up fields i wanna analyze and feed data into
video_list = []
video_title = []
video_candidate = []
video_channel = []

#get data from youtube v3 api
for x in candidates:
    i = 0
    page_token = ''
    while i < 5:
        nextpage = 'pageToken=' + page_token
        req = youtube_search+'&'+key+'&'+part_search+'&'+order_views+'&'+max_results+'&q='+x+'&'+date_filter+'&'+nextpage
        print(req)
        search_items = json.loads(urllib.request.urlopen(req).read())
        page_token = search_items['nextPageToken']

        for j in search_items['items']:
            try:
                videoid = j['id']['videoId']
                channelid = j['id']['channelId']
                videotitle = j['snippet']['title']
                video_list.append(videoid)
                video_candidate.append(x)
                video_title.append(videotitle)
                video_channel.append(channelid)
            except:
                break        
        i += 1

analysis = pd.DataFrame(columns = ['Candidate','Video ID','Channel ID','Video Title'])
analysis['Candidate'] = video_candidate
analysis['Video ID'] = video_list
analysis['Video Title'] = video_title
analysis['Channel ID'] = video_channel


analysis.to_excel('candidate_yt_vids.xlsx')
print('done')

    




