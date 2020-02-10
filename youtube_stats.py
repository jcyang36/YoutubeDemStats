#We break this out into separate files because of YouTube API Quota Limit
import pandas as pd
import urllib.request
import json

#api key
key = "key=YOURKEYHERE"

#video api and params
youtube_vid_stats = "https://www.googleapis.com/youtube/v3/videos?"
part_stats = "part=statistics"

video_views = []
video_likes = []
video_dislikes = []
video_comments = []

video_list = pd.read_excel('candidate_yt_vids.xlsx')
ids = video_list['Video ID']

for i in ids:
    req = youtube_vid_stats+'&'+key+'&'+part_stats+'&id='+i
    search_items = json.loads(urllib.request.urlopen(req).read())
    print(req)
    if search_items['pageInfo']['totalResults'] == 0:
        views = 'removed'
        likes = 'removed'
        dislikes = 'removed'
        comments = 'removed'
    else:
        stats = search_items['items'][0]['statistics']
        views = stats['viewCount']
        try:
            likes = stats['likeCount']
        except:
            likes = 'disabled'
        try:
            dislikes = stats['dislikeCount']
        except:
            dislikes = 'disabled'
        try:
            comments = stats['commentCount']
        except:
            comments = 'disabled'
    video_views.append(views)
    video_likes.append(likes)
    video_dislikes.append(dislikes)
    video_comments.append(comments)

video_list['views'] = video_views
video_list['likes'] = video_likes
video_list['dislikes'] = video_dislikes
video_list['comments'] = video_comments

video_list.to_excel('candidate_yt_statistics.xlsx')
print('done')

