__author__ = 'dientoan'
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users

class dbsongs(ndb.Model):
  title = ndb.StringProperty()
  creator  = ndb.StringProperty()
  location  = ndb.StringProperty()
  lyric  = ndb.StringProperty()
  ngaynhap =ndb.DateTimeProperty(auto_now_add=True)

class Log(ndb.Model):
    access_time = ndb.DateTimeProperty(auto_now_add=True)
    ip_address = ndb.StringProperty()