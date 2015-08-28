__author__ = 'dientoan'
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users
class dbsongs(ndb.Model):
  title = ndb.StringProperty()
  creator  = ndb.StringProperty()
  location  = ndb.StringProperty()
  lyric  = ndb.StringProperty()
