from urllib.request import urlopen
from bs4 import BeautifulSoup
import htmlDelet as Delhtm


def Total_kill(name_user):
    url = "https://r6.op.gg/search?search={}".format(name_user)
    result = urlopen(url)
    html = result.read()
    soup = BeautifulSoup(html, 'html.parser')
    tag = str(soup.find_all(class_="red")[0])
    REtag = Delhtm.remove_tag(tag)
    return REtag

def Total_death(name_user):
    url = "https://r6.op.gg/search?search={}".format(name_user)
    result = urlopen(url)
    html = result.read()
    soup = BeautifulSoup(html, 'html.parser')
    tag = str(soup.find_all(class_="red")[1])
    REtag = Delhtm.remove_tag(tag)
    return REtag


print('R6S : Ready')



