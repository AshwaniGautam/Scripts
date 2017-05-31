from facepy import GraphAPI
import datetime, time

def get_key(item):
    return item['created_time']

def change_creation_time():

    for post in posts:

        post_time = post['created_time'].split('+')[0]
        created_time = time.mktime(datetime.datetime.strptime(post_time, "%Y-%m-%dT%H:%M:%S").timetuple())
        post['created_time'] = created_time


Access_Token = "Your_Access_Token"
graph = GraphAPI(Access_Token, version='2.9')

while 1:

    posts = graph.get("Group-ID/feed?fields=created_time,reactions,message&limit=100")['data']
    flag = 0
    Deadline = time.time() - 6*3600  # carefull change according to timezone
    Lower_Bound = time.time() - 7*3600

    while 1:

        change_creation_time()
        posts.sort(key=get_key, reverse=True)

        for post in posts:

            if Lower_Bound <= post['created_time']:
                if post['created_time'] < Deadline:
                    if len(post['reactions']['data']) < 5:
                        graph.delete(str(post['id']))
            else:
                flag = 1
                time.sleep(480)
                break
        if flag:
            break

        if 'paging' in Group_Handle and 'next' in Group_Handle['paging']:
            request_str = Group_Handle['paging']['next'].replace('https://graph.facebook.com/v2.9', '')
            Group_Handle = graph.get(request_str)
