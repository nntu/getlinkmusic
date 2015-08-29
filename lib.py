__author__ = 'tunn1'

from google.appengine.api import urlfetch
import re
from lxml import etree
def nhaccuatui_new(url):
    listnhac = []
    response = urlfetch.fetch(url)
    the_page = response.content
    p = re.compile(r"http://www.nhaccuatui.com/flash/xml([?\&\d\w=\d]*)")
    xmlurl = p.search(the_page).group()
    xmlpage = urlfetch.fetch(xmlurl)
    tree = etree.fromstring(xmlpage.content)
    for node in tree.iter('track'):
        title = node.find('title').text.strip()
        creator  = node.find('creator').text.strip()
        location  = node.find('location').text.strip()
        lyric  = node.find('lyric').text.strip()
        listnhac.append({'title':title,'creator':creator,'location':location,'lyric':lyric})
    return listnhac

