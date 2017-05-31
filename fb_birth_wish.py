import requests
import json
import facepy

def get_friend_list(access, url, para):
    r = requests.get(url, params = para)
    results = json.loads(r.text)
    return results['data']
    
def post_on_wall():
    pass    


def main():
    ACCESS_TOKEN = "Insert Access Token"
    base_url = "https://graph.facebook.com/me/friends"
    url = "https://graph.facebook.com/fql"
    para = {"access_token" : ACCESS_TOKEN}
    listi = get_friend_list(ACCESS_TOKEN, base_url, para)
    
    for i in listi:
        print i['name'], "---->",
        query = "SELECT birthday FROM user WHERE uid = %s" % (i['id']) 
        r = requests.get(url, params = {'q' : query, 'access_token' : ACCESS_TOKEN})
        results = json.loads(r.text)
        print results['data'][0]['birthday']
        
    
if __name__ == "__main__":
    main()
    user = "lwmarsh06@gmail.com"

#1526116847416582 something
#1557908431109798 Punner Janam


















password = "ash@iitk1"
