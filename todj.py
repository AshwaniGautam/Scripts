from facepy import GraphAPI
import datetime

Access_Token = "Insert-Your-Access_Token"
graph = GraphAPI(Access_Token)
Deadline = (datetime.datetime.utcnow()-datetime.timedelta(minutes=60)).strftime("%Y-%m-%dT%H:%M:%S")
Lower_Bound = (datetime.datetime.utcnow()-datetime.timedelta(minutes=500)).strftime("%Y-%m-%dT%H:%M:%S")

Group_Handle = graph.get("1121167991289664/feed?since="+Lower_Bound+"&until="+Deadline)
for post in Group_Handle['data']:
    if post.has_key('message' or 'story'):
        if len(graph.get(str(post['id'])+'/likes')['data']) <= 20:
            graph.post(str(post['id'])+"/comments", message='kdkd')



