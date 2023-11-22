#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install --upgrade google-api-python-client


# In[7]:


from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns


# In[8]:


api_key='AIzaSyAj6J0tPowYHdLDeS7SqgSJFVh6PAtASJM'
#channel_id='UC-CBQChrXvLzYc9oxpMfFPg'
channel_ids=['UC-CBQChrXvLzYc9oxpMfFPg', #Naa anveshana
            'UCrd9nnfKqHtpB_Gyg8xBwaw',#bankokpilla,
            'UCPKNKldggioffXPkSmjs5lQ',#hamzy mukbang
            'UCBwmMxybNva6P_5VmxjzwqA', #apna college
            'UCnz-ZXXER4jOvuED5trXfEA']# TechTFQ]
youtube =build('youtube','v3',developerKey=api_key)


# #Function to get channel statistics
# 

# In[16]:


def get_channel_stats(youtube,channel_ids):
    all_data=[]
    request = youtube.channels().list(
    part ='snippet,contentDetails,statistics',
    id=','.join(channel_ids))
    response = request.execute()
    for i in range(len(response['items'])):
        data=dict(Channel_name=response['items'][i]['snippet']['title'],
              Subscribers = response['items'][i]['statistics']['subscriberCount'],
              Views= response['items'][i]['statistics']['viewCount'],
              Total_video= response['items'][i]['statistics']['videoCount'],
              Playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads']
                 )
        all_data.append(data)
    
        
    
    
    return all_data

    
    


# In[17]:


channels_statistics=get_channel_stats(youtube,channel_ids)


# In[18]:


channels_data=pd.DataFrame(channels_statistics)


# In[19]:


channels_data


# In[20]:


channels_data.dtypes


# Since the data type is currently set to 'object', we need to convert the relevant columns into integer format before we can effectively visualize the data.....🫠🤦‍♀️

# In[21]:


channels_data['Subscribers']=pd.to_numeric(channels_data['Subscribers'])
channels_data['Views']=pd.to_numeric(channels_data['Views'])
channels_data['Total_video']=pd.to_numeric(channels_data['Total_video'])
channels_data.dtypes


# successfully converted🤝🏼

# #For visualization i am using seaborn🌊....

# In[23]:


sns.set(rc={'figure.figsize':(10,8)})
ax=sns.barplot(x='Channel_name',y='Subscribers',data=channels_data)


# In[24]:


sns.set(rc={'figure.figsize':(12,10)})
ax=sns.barplot(x='Channel_name',y='Views',data=channels_data)


# In[25]:



sns.set(rc={'figure.figsize':(12,10)})
ax=sns.barplot(x='Channel_name',y='Total_video',data=channels_data)


# # Output for the above response ....which helps us to konow the formatte and get the required data..it is JSON formatted💪🏻
# {
#    "kind":"youtube#channelListResponse",
#    "etag":"9LcHkXRtb-WB9krdfBKkLU8Jzrg",
#    "pageInfo":{
#       "totalResults":5,
#       "resultsPerPage":5
#    },
#    "items":[
#       {
#          "kind":"youtube#channel",
#          "etag":"kjV4pq7zox6sZO8vcvEJIjrGYGc",
#          "id":"UC-CBQChrXvLzYc9oxpMfFPg",
#          "snippet":{
#             "title":"Naa Anveshana",
#             "description":"నమస్తే ఫ్రెండ్స్ నా పేరు అన్వేష్ నేను ప్రపంచ యాత్రికుడిని వెల్కమ్ టు మై ఛానల్ నా అన్వేషణ నా కళ్ళతో మీకు చూపిస్తాను ప్రపంచాన్ని\n\nCounting : 🇺🇸 🇨🇦 🇪🇸 🇫🇷🇪🇹 🇪🇺🇨🇳🇯🇲🇶🇦🇷🇺🇵🇹🇱🇨🇰🇳🇰🇷🇬🇧🇯🇵🇦🇬🇧🇸🇧🇧🇧🇪🇲🇽🇧🇿🇨🇴🇻🇮🏴\\U000e0067\\U000e0062\\U000e0065\\U000e006e\\U000e0067\\U000e007f🇬🇷🇭🇹🇭🇳🇭🇰🇻🇦🇮🇪🇮🇹🇲🇾🇵🇷🇫🇷🇸🇽🏳️\u200d🌈🇰🇳🇦🇪🇸🇴 🇩🇯🇹🇷 🇷🇸 🇽🇰 🇲🇪 🇧🇦 🇦🇲🇵🇦🇨🇷🇵🇪🇧🇷🇸🇻🇦🇷🇦🇶🇵🇾🇨🇺🇹🇿🇲🇷🇦🇫🇺🇿🇯🇴🇬🇪🇹🇭🇲🇺🇲🇬🇦🇺🇫🇯🇻🇺🇼🇸🇹🇻🇹🇴\n\nనా పేరు అన్వేష్ నేను వైజాగ్ అబ్బాయిని నేను ట్రావెలింగ్ అండ్ టూరిజం లో పోస్ట్ గ్రాడ్యుయేషన్ చేశాను నాకు ట్రావెలింగ్ అంటే చాలా ఇష్టం ఇప్పటివరకు 85 దేశాలు తిరిగాను ప్రపంచంలో ఉన్న దేశాలు అన్నీ తిరిగి అవి మీకు చూపించాలి అనేదే నా లక్ష్యం\n\n\nMy Mail \nNaaAnveshanaaa@gmail.com\n+91 70754 26329",
#             "customUrl":"@naaanveshana",
#             "publishedAt":"2019-08-20T08:09:37Z",
#             "thumbnails":{
#                "default":{
#                   "url":"https://yt3.ggpht.com/DLer1VC9KzQIOiTYFPrNXSndwrgXHplj6e4r0_JNkPcTaB0PfRwDQTPGWhhXoA12JiSGi991rCU=s88-c-k-c0x00ffffff-no-rj",
#                   "width":88,
#                   "height":88
#                },
#                "medium":{
#                   "url":"https://yt3.ggpht.com/DLer1VC9KzQIOiTYFPrNXSndwrgXHplj6e4r0_JNkPcTaB0PfRwDQTPGWhhXoA12JiSGi991rCU=s240-c-k-c0x00ffffff-no-rj",
#                   "width":240,
#                   "height":240
#                },
#                "high":{
#                   "url":"https://yt3.ggpht.com/DLer1VC9KzQIOiTYFPrNXSndwrgXHplj6e4r0_JNkPcTaB0PfRwDQTPGWhhXoA12JiSGi991rCU=s800-c-k-c0x00ffffff-no-rj",
#                   "width":800,
#                   "height":800
#                }
#             },
#             "localized":{
#                "title":"Naa Anveshana",
#                "description":"నమస్తే ఫ్రెండ్స్ నా పేరు అన్వేష్ నేను ప్రపంచ యాత్రికుడిని వెల్కమ్ టు మై ఛానల్ నా అన్వేషణ నా కళ్ళతో మీకు చూపిస్తాను ప్రపంచాన్ని\n\nCounting : 🇺🇸 🇨🇦 🇪🇸 🇫🇷🇪🇹 🇪🇺🇨🇳🇯🇲🇶🇦🇷🇺🇵🇹🇱🇨🇰🇳🇰🇷🇬🇧🇯🇵🇦🇬🇧🇸🇧🇧🇧🇪🇲🇽🇧🇿🇨🇴🇻🇮🏴\\U000e0067\\U000e0062\\U000e0065\\U000e006e\\U000e0067\\U000e007f🇬🇷🇭🇹🇭🇳🇭🇰🇻🇦🇮🇪🇮🇹🇲🇾🇵🇷🇫🇷🇸🇽🏳️\u200d🌈🇰🇳🇦🇪🇸🇴 🇩🇯🇹🇷 🇷🇸 🇽🇰 🇲🇪 🇧🇦 🇦🇲🇵🇦🇨🇷🇵🇪🇧🇷🇸🇻🇦🇷🇦🇶🇵🇾🇨🇺🇹🇿🇲🇷🇦🇫🇺🇿🇯🇴🇬🇪🇹🇭🇲🇺🇲🇬🇦🇺🇫🇯🇻🇺🇼🇸🇹🇻🇹🇴\n\nనా పేరు అన్వేష్ నేను వైజాగ్ అబ్బాయిని నేను ట్రావెలింగ్ అండ్ టూరిజం లో పోస్ట్ గ్రాడ్యుయేషన్ చేశాను నాకు ట్రావెలింగ్ అంటే చాలా ఇష్టం ఇప్పటివరకు 85 దేశాలు తిరిగాను ప్రపంచంలో ఉన్న దేశాలు అన్నీ తిరిగి అవి మీకు చూపించాలి అనేదే నా లక్ష్యం\n\n\nMy Mail \nNaaAnveshanaaa@gmail.com\n+91 70754 26329"
#             },
#             "country":"IN"
#          },
#          "contentDetails":{
#             "relatedPlaylists":{
#                "likes":"",
#                "uploads":"UU-CBQChrXvLzYc9oxpMfFPg"
#             }
#          },
#          "statistics":{
#             "viewCount":"426657273",
#             "subscriberCount":"1670000",
#             "hiddenSubscriberCount":false,
#             "videoCount":"1042"
#          }
#       },
#        {
#          "kind":"youtube#channel",
#          "etag":"V9cICDpljlEkttEopK_R89u5AUg",
#          "id":"UCBwmMxybNva6P_5VmxjzwqA",
#          "snippet":{
#             "title":"Apna College",
#             "description":"I'm Shradha, Ex-Microsoft Software Engineer, DRDO. My journey started from a small village of Haryana, in college I learned coding and got 2 internships at Microsoft, work for DRDO, invited for Google SPS and a Full Time Offer from Microsoft. I believe that skills are more important today and want to help students to learn & crack their dream companies ❤️\nSo, I left my Microsoft Job and started to teach students. I love my students and I love sharing my learnings.\nTo Chalo Phodte hain!\n\n\nFeel free to contact Shradha Didi for Seminars, Hackathons & Collaborations at the given email id below.\n\n\n",
#             "customUrl":"@apnacollegeofficial",
#             "publishedAt":"2020-08-05T16:09:28.304314Z",
#             "thumbnails":{
#                "default":{
#                   "url":"https://yt3.ggpht.com/nhDLqeIgXMJBDIrX2bXavvHoWX0tsslDEh7k2xZ1P0W8b_CMRVigp2kxJubYEVwBcBlogZDe=s88-c-k-c0x00ffffff-no-rj",
#                   "width":88,
#                   "height":88
#                },
#                "medium":{
#                   "url":"https://yt3.ggpht.com/nhDLqeIgXMJBDIrX2bXavvHoWX0tsslDEh7k2xZ1P0W8b_CMRVigp2kxJubYEVwBcBlogZDe=s240-c-k-c0x00ffffff-no-rj",
#                   "width":240,
#                   "height":240
#                },
#                "high":{
#                   "url":"https://yt3.ggpht.com/nhDLqeIgXMJBDIrX2bXavvHoWX0tsslDEh7k2xZ1P0W8b_CMRVigp2kxJubYEVwBcBlogZDe=s800-c-k-c0x00ffffff-no-rj",
#                   "width":800,
#                   "height":800
#                }
#             },
#             "localized":{
#                "title":"Apna College",
#                "description":"I'm Shradha, Ex-Microsoft Software Engineer, DRDO. My journey started from a small village of Haryana, in college I learned coding and got 2 internships at Microsoft, work for DRDO, invited for Google SPS and a Full Time Offer from Microsoft. I believe that skills are more important today and want to help students to learn & crack their dream companies ❤️\nSo, I left my Microsoft Job and started to teach students. I love my students and I love sharing my learnings.\nTo Chalo Phodte hain!\n\n\nFeel free to contact Shradha Didi for Seminars, Hackathons & Collaborations at the given email id below.\n\n\n"
#             }
#          },
#          "contentDetails":{
#             "relatedPlaylists":{
#                "likes":"",
#                "uploads":"UUBwmMxybNva6P_5VmxjzwqA"
#             }
#          },
#          "statistics":{
#             "viewCount":"672238070",
#             "subscriberCount":"4400000",
#             "hiddenSubscriberCount":false,
#             "videoCount":"772"
#          }
#       },
#              {
#          "kind":"youtube#channel",
#          "etag":"vonv5WsQGxytZ82lc3bsbbwKZDs",
#          "id":"UCnz-ZXXER4jOvuED5trXfEA",
#          "snippet":{
#             "title":"techTFQ",
#             "description":"Hi, I am Thoufiq! On this channel, I teach SQL, Python and Database concepts in the field of Data Analytics and Data Science in the most simplest manner possible. If this excites you then do consider subscribing.\n\nYou will also find videos covering interview questions and also videos where I provide career guidance in the field of Data Analytics and Data Science which should help you find your dream job.\n\nI aim to make techTFQ a go to YouTube channel for anyone learning SQL, Python and Databases in the field of Data Analytics and Data Science.\n\nThank you for begin here :)\n",
#             "customUrl":"@techtfq",
#             "publishedAt":"2020-06-13T05:20:37.182391Z",
#             "thumbnails":{
#                "default":{
#                   "url":"https://yt3.ggpht.com/68QpkOCRQespfOQ5yZwhCrM6Ab0kipqOU16JwAAhDm9f8I0CfPzMW-qpzdYJmn0TQ-UBd862=s88-c-k-c0x00ffffff-no-rj",
#                   "width":88,
#                   "height":88
#                },
#                "medium":{
#                   "url":"https://yt3.ggpht.com/68QpkOCRQespfOQ5yZwhCrM6Ab0kipqOU16JwAAhDm9f8I0CfPzMW-qpzdYJmn0TQ-UBd862=s240-c-k-c0x00ffffff-no-rj",
#                   "width":240,
#                   "height":240
#                },
#                "high":{
#                   "url":"https://yt3.ggpht.com/68QpkOCRQespfOQ5yZwhCrM6Ab0kipqOU16JwAAhDm9f8I0CfPzMW-qpzdYJmn0TQ-UBd862=s800-c-k-c0x00ffffff-no-rj",
#                   "width":800,
#                   "height":800
#                }
#             },
#             "localized":{
#                "title":"techTFQ",
#                "description":"Hi, I am Thoufiq! On this channel, I teach SQL, Python and Database concepts in the field of Data Analytics and Data Science in the most simplest manner possible. If this excites you then do consider subscribing.\n\nYou will also find videos covering interview questions and also videos where I provide career guidance in the field of Data Analytics and Data Science which should help you find your dream job.\n\nI aim to make techTFQ a go to YouTube channel for anyone learning SQL, Python and Databases in the field of Data Analytics and Data Science.\n\nThank you for begin here :)\n"
#             },
#             "country":"MY"
#          },
#          "contentDetails":{
#             "relatedPlaylists":{
#                "likes":"",
#                "uploads":"UUnz-ZXXER4jOvuED5trXfEA"
#             }
#          },
#          "statistics":{
#             "viewCount":"12525040",
#             "subscriberCount":"242000",
#             "hiddenSubscriberCount":false,
#             "videoCount":"98"
#          }
#       },
#              {
#          "kind":"youtube#channel",
#          "etag":"1gb6EJZkn956R-UPL4XUvbl5Fp8",
#          "id":"UCrd9nnfKqHtpB_Gyg8xBwaw",
#          "snippet":{
#             "title":"Bangkok Pilla",
#             "description":"Hello, nenu Sravani. living in Bangkok. I do videos about our life style in Thailand, Thailand culture, food and travel information. \nPlease subscribe and support. \nthank you. Namasthe 🙏🙏 \n\nyoutube channel - bangkok pilla\ninstagram - bangkok.pilla\n\nBangkok telugu vlogs",
#             "customUrl":"@bangkokpilla",
#             "publishedAt":"2022-01-25T05:52:00.227523Z",
#             "thumbnails":{
#                "default":{
#                   "url":"https://yt3.ggpht.com/n2l5miyBJlgVYrPEm9lVIBksNdCwK51-CIo37UQjF8zxZAIpeKthnR4OxXI_9HxgRxLY6ll7=s88-c-k-c0x00ffffff-no-rj",
#                   "width":88,
#                   "height":88
#                },
#                "medium":{
#                   "url":"https://yt3.ggpht.com/n2l5miyBJlgVYrPEm9lVIBksNdCwK51-CIo37UQjF8zxZAIpeKthnR4OxXI_9HxgRxLY6ll7=s240-c-k-c0x00ffffff-no-rj",
#                   "width":240,
#                   "height":240
#                },
#                "high":{
#                   "url":"https://yt3.ggpht.com/n2l5miyBJlgVYrPEm9lVIBksNdCwK51-CIo37UQjF8zxZAIpeKthnR4OxXI_9HxgRxLY6ll7=s800-c-k-c0x00ffffff-no-rj",
#                   "width":800,
#                   "height":800
#                }
#             },
#             "localized":{
#                "title":"Bangkok Pilla",
#                "description":"Hello, nenu Sravani. living in Bangkok. I do videos about our life style in Thailand, Thailand culture, food and travel information. \nPlease subscribe and support. \nthank you. Namasthe 🙏🙏 \n\nyoutube channel - bangkok pilla\ninstagram - bangkok.pilla\n\nBangkok telugu vlogs"
#             },
#             "country":"TH"
#          },
#          "contentDetails":{
#             "relatedPlaylists":{
#                "likes":"",
#                "uploads":"UUrd9nnfKqHtpB_Gyg8xBwaw"
#             }
#          },
#          "statistics":{
#             "viewCount":"1176745876",
#             "subscriberCount":"2610000",
#             "hiddenSubscriberCount":false,
#             "videoCount":"249"
#          }
#       },
#           {
#          "kind":"youtube#channel",
#          "etag":"RmIUkdRyMcC3B-7br0EGNqAvgGA",
#          "id":"UCPKNKldggioffXPkSmjs5lQ",
#          "snippet":{
#             "title":"[햄지]Hamzy",
#             "description":"❤대리만족 1,000%%% 햄지Hamzy's Mukbang❤\n\n비지니스 문의:\nhamzy3390@gmail.com\n",
#             "customUrl":"@hamzymukbang",
#             "publishedAt":"2012-09-25T08:54:01Z",
#             "thumbnails":{
#                "default":{
#                   "url":"https://yt3.ggpht.com/cNxSPvaC9i73N-XNkZhnbQ3xIJ0PrUS2FfxY7Kl4HmPl_ZU2M8DIedaXdM0kh7a40_Hzhenqfg=s88-c-k-c0x00ffffff-no-rj",
#                   "width":88,
#                   "height":88
#                },
#                "medium":{
#                   "url":"https://yt3.ggpht.com/cNxSPvaC9i73N-XNkZhnbQ3xIJ0PrUS2FfxY7Kl4HmPl_ZU2M8DIedaXdM0kh7a40_Hzhenqfg=s240-c-k-c0x00ffffff-no-rj",
#                   "width":240,
#                   "height":240
#                },
#                "high":{
#                   "url":"https://yt3.ggpht.com/cNxSPvaC9i73N-XNkZhnbQ3xIJ0PrUS2FfxY7Kl4HmPl_ZU2M8DIedaXdM0kh7a40_Hzhenqfg=s800-c-k-c0x00ffffff-no-rj",
#                   "width":800,
#                   "height":800
#                }
#             },
#             "localized":{
#                "title":"[햄지]Hamzy",
#                "description":"❤대리만족 1,000%%% 햄지Hamzy's Mukbang❤\n\n비지니스 문의:\nhamzy3390@gmail.com\n"
#             },
#             "country":"KR"
#          },
#          "contentDetails":{
#             "relatedPlaylists":{
#                "likes":"",
#                "uploads":"UUPKNKldggioffXPkSmjs5lQ"
#             }
#          },
#          "statistics":{
#             "viewCount":"4126164801",
#             "subscriberCount":"11800000",
#             "hiddenSubscriberCount":false,
#             "videoCount":"713"
#          }
#       }
#    ]
# }

# Function to get video ids

# In[27]:


channels_data


# In[28]:


playlist_id=channels_data.loc[channels_data['Channel_name']=='Naa Anveshana','Playlist_id'].iloc[0]


# In[98]:


#playlist_id


# In[29]:


def get_video_ids(youtube,playlist_id):
    request= youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50 #the purpose of this statement is return total 50 requests as youtube by default give 5 results only and more over 50 is the max value to pass
    )
    response= request.execute()
    video_ids=[]
    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])
    next_page_token=response.get('nextPageToken')
    more_pages=True
    while more_pages:
        if  next_page_token is None:
            more_pages=False
        else:
            request= youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId=playlist_id,
                    maxResults=50 ,#the purpose of this statement is return total 50 requests as youtube by default give 5 results only and more over 50 is the max value to pass
                    pageToken=next_page_token
            )
            response= request.execute()
            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
        
            next_page_token=response.get('nextPageToken')
            
    return video_ids


# In[30]:


video_ids=get_video_ids(youtube,playlist_id)


# In[31]:


video_ids


# #write a function that could extract the details from all the videos

# In[32]:


def get_video_details(youtube,video_ids):
    all_video_stats=[]
    
    for i in range(0,len(video_ids),50):
        request=youtube.videos().list(
        part='snippet,statistics',
        id=','.join(video_ids[i:i+50]))
        response = request.execute()
        for video in response['items']:
            video_stats=dict(Title=video['snippet']['title'],
                            Published_date=video['snippet']['publishedAt'],
                            Views=video['statistics']['viewCount'],
                            Likes=video['statistics']['likeCount'],
                           
                            Comments=video['statistics']['commentCount']
                             
                            )
            all_video_stats.append(video_stats)
            
    
    return all_video_stats


# In[33]:


video_details=get_video_details(youtube,video_ids)


# In[34]:


video_data=pd.DataFrame(video_details)


# In[35]:


video_data


# #output of the above above code the shows the required contents we want from the entire data..........
# {
#    "kind":"youtube#playlistItemListResponse",
#    "etag":"9a2u9pBXu0MUeFuSVw0bzAglZWA",
#    "nextPageToken":"EAAaIVBUOkNESWlFRGhETlVaQlJUWkNNVFkwT0RFelF6Z29BUQ",
#    "items":[
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"SuPPfNWMsVqhtyxE99iv0LZE6zQ",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLk10amY4Y1l3UWlr",
#          "contentDetails":{
#             "videoId":"Mtjf8cYwQik",
#             "videoPublishedAt":"2023-10-13T02:30:09Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"lmj2Pw1uZQmtRu4CtM6IVYhE8Xw",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLlFaUlF6TDlOYUN3",
#          "contentDetails":{
#             "videoId":"QZRQzL9NaCw",
#             "videoPublishedAt":"2023-10-10T02:30:48Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"HrcE5JkrGkmzSPJNGPJmqiYdaWE",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLlBuVENIa3d3RTI4",
#          "contentDetails":{
#             "videoId":"PnTCHkwwE28",
#             "videoPublishedAt":"2023-10-07T02:30:20Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"II2Ftg2STuy4NilfYtehw_o_rnw",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLmVQSmkwNURYbFA4",
#          "contentDetails":{
#             "videoId":"ePJi05DXlP8",
#             "videoPublishedAt":"2023-10-05T02:30:17Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"E4WF4ZmLfOTxU_KyjAr6Wbzwxh0",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLjE3a3FBbkk1VDVn",
#          "contentDetails":{
#             "videoId":"17kqAnI5T5g",
#             "videoPublishedAt":"2023-10-03T02:30:00Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"uQJEpDxiO8Lp7-Plyv-n3SvCzE0",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLlVtcm05RS1IVVVF",
#          "contentDetails":{
#             "videoId":"Umrm9E-HUUE",
#             "videoPublishedAt":"2023-10-01T02:30:11Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"Yx3HgEmoBs2r-NJ-owoiK2EUyL8",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLlFKY3h1N0RuWG1Z",
#          "contentDetails":{
#             "videoId":"QJcxu7DnXmY",
#             "videoPublishedAt":"2023-09-29T02:30:10Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"ca5HYrKSzyIeITuOzAjl4APAGmc",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLlFsQ0xLeERhcHlV",
#          "contentDetails":{
#             "videoId":"QlCLKxDapyU",
#             "videoPublishedAt":"2023-09-26T02:30:10Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"_A6-_g7klwobWnrdISiU6tZioJQ",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLkt0dnI5Tlp5Mjlr",
#          "contentDetails":{
#             "videoId":"Ktvr9NZy29k",
#             "videoPublishedAt":"2023-09-24T02:29:53Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"hRn4d-iALQ2qb0UaXUDm3ZTV5UM",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLml5Mi13cHZjNDkw",
#          "contentDetails":{
#             "videoId":"iy2-wpvc490",
#             "videoPublishedAt":"2023-09-21T02:30:17Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"hMy1xFy-e-O0GnxWopI2Pe9Ovng",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLjVObVFPS1NNcWlv",
#          "contentDetails":{
#             "videoId":"5NmQOKSMqio",
#             "videoPublishedAt":"2023-09-19T02:30:02Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"wjnpsIwKANpy1A4I_mzQAkvOHZg",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLlZUVXJzY0t3Nktj",
#          "contentDetails":{
#             "videoId":"VTUrscKw6Kc",
#             "videoPublishedAt":"2023-09-16T02:30:23Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"PWYDQoSfu3ORiqnr34JhnCPmmKI",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLm5NajFySTZXSlBB",
#          "contentDetails":{
#             "videoId":"nMj1rI6WJPA",
#             "videoPublishedAt":"2023-09-14T03:44:36Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"8PSW3qoxxP0c7Kw7Na5sjJOX6FI",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLmNsVGFmc1FQbHBz",
#          "contentDetails":{
#             "videoId":"clTafsQPlps",
#             "videoPublishedAt":"2023-09-12T02:30:19Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"fRUXYhih-UZ7dCl9ZdSn3Xg6d_U",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLm5Nd3poLWttMkJJ",
#          "contentDetails":{
#             "videoId":"nMwzh-km2BI",
#             "videoPublishedAt":"2023-09-10T02:50:57Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"KUiAiJQfJGz87u50tzrgCIpaYdU",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLkNfNWs0S0IzUmJB",
#          "contentDetails":{
#             "videoId":"C_5k4KB3RbA",
#             "videoPublishedAt":"2023-09-09T00:14:10Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"l_rspT2Q7Xc-sB0fXjp2FuUlCA8",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLmxncUlyOGxvZTdj",
#          "contentDetails":{
#             "videoId":"lgqIr8loe7c",
#             "videoPublishedAt":"2023-09-07T02:30:20Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"muMqEi8OfyW23cTN-jURXiR3Ij0",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLmNBNzNtcXVEMXp3",
#          "contentDetails":{
#             "videoId":"cA73mquD1zw",
#             "videoPublishedAt":"2023-09-05T02:30:26Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"NEEVPrAx6FkzxjRz6V04_A2NPOU",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLnN6aXpCQmVKMmNv",
#          "contentDetails":{
#             "videoId":"szizBBeJ2co",
#             "videoPublishedAt":"2023-09-03T02:30:24Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"0VUB4J_0WhlKkYL3lg3IJvl1Cro",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLjN1cTBMck9SZ2RJ",
#          "contentDetails":{
#             "videoId":"3uq0LrORgdI",
#             "videoPublishedAt":"2023-09-01T02:30:02Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"OhWYOAVpfZ_NHajswZ6htSFH-V8",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLlBGa1hQRmk1QUJj",
#          "contentDetails":{
#             "videoId":"PFkXPFi5ABc",
#             "videoPublishedAt":"2023-08-30T02:30:18Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"uOzdlkX1KEQeRE8FzBxNtaeAk2A",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLmw2QzU5c3JVU2Nv",
#          "contentDetails":{
#             "videoId":"l6C59srUSco",
#             "videoPublishedAt":"2023-08-28T02:30:18Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"EwYdxyiFti89ihnn5jUEDb6f_Go",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLlVxUlQ4ZjdiNTlV",
#          "contentDetails":{
#             "videoId":"UqRT8f7b59U",
#             "videoPublishedAt":"2023-08-26T02:30:09Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"pmpesybI1aghkj6SJPt1xveSrVw",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLmQxajByR0czNk44",
#          "contentDetails":{
#             "videoId":"d1j0rGG36N8",
#             "videoPublishedAt":"2023-08-24T02:30:15Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"JBsgJsNdqrzJo1aHitXLUQR59bU",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLkVGMEk0NVJmREhZ",
#          "contentDetails":{
#             "videoId":"EF0I45RfDHY",
#             "videoPublishedAt":"2023-08-22T02:30:05Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"96IAAo-SMbnOSwkNnpMbpVKhHhc",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLjZmWWhObFRzZHVJ",
#          "contentDetails":{
#             "videoId":"6fYhNlTsduI",
#             "videoPublishedAt":"2023-08-19T04:52:05Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"sC1Uy8OjeF7_tPA8HwZQDom19a4",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLkJXV1N4QnJHMmZ3",
#          "contentDetails":{
#             "videoId":"BWWSxBrG2fw",
#             "videoPublishedAt":"2023-08-17T03:47:03Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"YOkw4nLvxThTS70tAAOAWNsGh4c",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLmo3U3N2Nno2bXlz",
#          "contentDetails":{
#             "videoId":"j7Ssv6z6mys",
#             "videoPublishedAt":"2023-08-15T02:30:31Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"rmy41uFpH1xJvIZz_7vwopndDDk",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLlZrNkNMcjNiSDJj",
#          "contentDetails":{
#             "videoId":"Vk6CLr3bH2c",
#             "videoPublishedAt":"2023-08-12T12:49:37Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"kSqAViIcmhhomcYyyBoRgjALToc",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLlg2dFIzQWw3Yzhv",
#          "contentDetails":{
#             "videoId":"X6tR3Al7c8o",
#             "videoPublishedAt":"2023-08-09T11:30:15Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"8bpIm8WHEc2EDKZiyktIzuokpSU",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLkhUVU5PWUlndHVZ",
#          "contentDetails":{
#             "videoId":"HTUNOYIgtuY",
#             "videoPublishedAt":"2023-08-07T03:01:24Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"J8oRj4HVpsedZo9b42srcvMzlaE",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLjUtNkFvb0hWRUJr",
#          "contentDetails":{
#             "videoId":"5-6AooHVEBk",
#             "videoPublishedAt":"2023-08-05T04:32:22Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"3MfIPJvBrcjbFQUbmd9o0RIn9GY",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLk9HWlRNVUFaQXRB",
#          "contentDetails":{
#             "videoId":"OGZTMUAZAtA",
#             "videoPublishedAt":"2023-08-03T06:00:55Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"FEiC-5GKeazG-UY3zuWfjnwXdSs",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLng0MVVoYjM4T01v",
#          "contentDetails":{
#             "videoId":"x41Uhb38OMo",
#             "videoPublishedAt":"2023-08-01T05:56:52Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"qE-SuwmYne3z2bkBjEfZ_3oYpNs",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLnZjSHVxV0pvREpB",
#          "contentDetails":{
#             "videoId":"vcHuqWJoDJA",
#             "videoPublishedAt":"2023-07-30T08:04:10Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"D9U101HUJy5Drvjx6ahT6sD3Gb8",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLjQzdDdXdEw2S01R",
#          "contentDetails":{
#             "videoId":"43t7WtL6KMQ",
#             "videoPublishedAt":"2023-07-29T04:10:20Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"fDivgEZrIUF8m9y0bl3IkZM-G5s",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLkFVZ2VMdmsySFg0",
#          "contentDetails":{
#             "videoId":"AUgeLvk2HX4",
#             "videoPublishedAt":"2023-07-27T04:54:21Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"lDeghBJ4mExOgavS54XXSNnkX8M",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLmhpUXdfcW9mU1hr",
#          "contentDetails":{
#             "videoId":"hiQw_qofSXk",
#             "videoPublishedAt":"2023-07-24T05:16:41Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"SfNwEwRF3vTU1cQeKbNu3VhQyaM",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLko3NFcwOHBWR1Jj",
#          "contentDetails":{
#             "videoId":"J74W08pVGRc",
#             "videoPublishedAt":"2023-07-23T09:26:34Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"wyeWdxONAK2HycsotwD92inhQnw",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLmtUTnR2SzFtN0R3",
#          "contentDetails":{
#             "videoId":"kTNtvK1m7Dw",
#             "videoPublishedAt":"2023-07-22T04:32:37Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"bVzpKMjOpyjgAIw634pgNYKiVwY",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLmJzUncwR1ZmUk5Z",
#          "contentDetails":{
#             "videoId":"bsRw0GVfRNY",
#             "videoPublishedAt":"2023-07-20T04:27:26Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"vlqzsq6981ZuvI6ctfZIbM_Esfw",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLmRIZ2tEUU9qSG1v",
#          "contentDetails":{
#             "videoId":"dHgkDQOjHmo",
#             "videoPublishedAt":"2023-07-18T03:15:23Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"sFofBVjhxQwEHpHsl6kYgLEJihU",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLmkwQW1saXJIUlBJ",
#          "contentDetails":{
#             "videoId":"i0AmlirHRPI",
#             "videoPublishedAt":"2023-07-15T02:30:18Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"mv7zB4YJcTSyUsxB2cA663L04gg",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLndrU2M4cm5uRHVZ",
#          "contentDetails":{
#             "videoId":"wkSc8rnnDuY",
#             "videoPublishedAt":"2023-07-11T03:00:22Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"JnRRZ5hZX1VIfIdXbvXMRHnKnlk",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLjZBYWR0c0dfRmtv",
#          "contentDetails":{
#             "videoId":"6AadtsG_Fko",
#             "videoPublishedAt":"2023-07-08T03:50:20Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"Xx26k8so9stLTUB3KW5two1LmSE",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLnRDUE1jXzZiMnVv",
#          "contentDetails":{
#             "videoId":"tCPMc_6b2uo",
#             "videoPublishedAt":"2023-07-05T02:30:24Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"nNdM7P5yyBA4XMps1CSkJ543Hos",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLmNBZV9mMkZLTHpn",
#          "contentDetails":{
#             "videoId":"cAe_f2FKLzg",
#             "videoPublishedAt":"2023-07-03T02:30:24Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"bAV3E7g88VO-Zt5r_I-SGynjc2c",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLlk2TXU0UzZOd1Rv",
#          "contentDetails":{
#             "videoId":"Y6Mu4S6NwTo",
#             "videoPublishedAt":"2023-07-01T02:30:26Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"v1olSP5Zw3Q2rao8yRgtX7ALQt0",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLllRbnk4QWxCYzRj",
#          "contentDetails":{
#             "videoId":"YQny8AlBc4c",
#             "videoPublishedAt":"2023-06-30T02:30:24Z"
#          }
#       },
#       {
#          "kind":"youtube#playlistItem",
#          "etag":"kMA6fLPED-vEaDuQ73JsIND7Kl8",
#          "id":"VVUtQ0JRQ2hyWHZMelljOW94cE1mRlBnLmZyU1V4bFdTc3ZJ",
#          "contentDetails":{
#             "videoId":"frSUxlWSsvI",
#             "videoPublishedAt":"2023-06-29T02:30:14Z"
#          }
#       }
#    ],
#    "pageInfo":{
#       "totalResults":1043,
#       "resultsPerPage":50
#    }
# }

# In[36]:


video_data['Published_date']=pd.to_datetime(video_data['Published_date']).dt.date
video_data['Views']=pd.to_numeric(video_data['Views'])
video_data['Likes']=pd.to_numeric(video_data['Likes'])
video_data['Comments']=pd.to_numeric(video_data['Comments'])
video_data


# In[37]:


video_data.dtypes


# In[38]:


top10_videos=video_data.sort_values(by='Views',ascending=False).head(10)


# In[39]:


top10_videos


# In[40]:


ax1=sns.barplot(x='Views',y='Title',data=top10_videos)


# In[41]:


video_data


# In[42]:


video_data['Month']=pd.to_datetime(video_data['Published_date']).dt.strftime('%b')


# In[43]:


video_data


# In[44]:


videos_per_month=video_data.groupby('Month',as_index=False).size()


# In[45]:


videos_per_month


# In[46]:


sort_order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']


# In[47]:


videos_per_month.index=pd.CategoricalIndex(videos_per_month['Month'],categories=sort_order,ordered=True)


# In[50]:


videos_per_month=videos_per_month.sort_index()


# In[51]:


ax2=sns.barplot(x='Month',y='size',data=videos_per_month)


# In[ ]:





# In[54]:


video_data.to_csv('Video_Details(Naa Anveshana).csv')

