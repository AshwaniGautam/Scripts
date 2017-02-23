import time
import urllib2
from bs4 import BeautifulSoup
import sys

try:
    import pynotify
except:
    raise "Pynotify not installed on your system.Type sudo apt-get install pynotify to install"

def Message(title, message):
    pynotify.init("Test")
    pop = pynotify.Notification(title, message)
    pop.show()
    return

def get_match():

    matches = soup.find_all('a', {"class" : "cb-font-12 cb-lv-scrs-well cb-lv-scrs-well-live"})
    sys.stdout.write("\nPlease select a match\n")
    j = 1
    for i in matches:
        print j, i.get('title')
        j += 1
    choice = int(sys.stdin.readline())
    return matches[choice-1].get('title')

def get_link(id):

    half_url = soup.find_all('a', {'title':id})[0].get('href')
    url = "http://www.cricbuzz.com"+half_url
    return url

def display_score(url):

    while 1:

        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'lxml')

        #msg1 = soup.find_all('h2', {'class':'cb-font-20 text-bold inline-block ng-binding'})[0].get_text()
        #print msg1, 'iop'
        msg2 =  soup.find_all('div', {'class':'cb-col-100 cb-col cb-col-scores'})[0].get_text()

        Message('Scores\n',  '\n' + msg2)

        time.sleep(300)


url = "http://www.cricbuzz.com/cricket-match/live-scores"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'lxml')
match = get_match()
url = get_link(match)
display_score(url)

