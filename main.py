#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import hashlib
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from dbsongs import dbsongs
from google.appengine.ext import ndb
from lib import *
import json
import jinja2
import logging
jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class MainHandler(webapp.RequestHandler):
    def get(self):
        foo, bar = "some", "enthralling text"
        template_values = {
          'some_foo': foo,
          'some_bar': bar
        }

        # make a new template instance
        templ = jinja_environment.get_template( 'index.html')
        # unpack the dictionary to become keyword arguments and render
        self.response.out.write(templ.render(**template_values))

class GetLinkHandler(webapp.RequestHandler):
    def post(self):

        url = self.request.get('tb_link')
        listlink = nhaccuatui_new(url)
        template_values = {
          'url': url,
          'listlink': listlink
        }


        # make a new template instance
        templ =  jinja_environment.get_template( 'getlink.html')
        # unpack the dictionary to become keyword arguments and render
        self.response.out.write(templ.render(**template_values))

class JsonHandler(webapp.RequestHandler):
    def post(self):

        url = self.request.get('tb_link')
        listlink = nhaccuatui_new(url)
        # try:
        #     for i in listlink:
        #         logging.info(i['title'])
        #         dbsongs.get_or_insert(title = i['title'],creator=i['creator'],location =i['location'], lyric= i['lyric'] )
        # except:
        #     logging.error('There was an error retrieving posts from the datastore')
        #     pass
        # for i in listlink:
        #     key = hashlib.md5(('%s:%s'% (i['title'],i['creator'])).encode('utf-8')).hexdigest()
        #     logging.info(key)
        #     sandy_key = ndb.Key(dbsongs,key)
        #     dbsongs.get_or_insert(sandy_key,title = i['title'],creator=i['creator'],location =i['location'], lyric= i['lyric'] )
        for i in listlink:
            query = dbsongs().query(dbsongs.creator== i['creator'] ,  dbsongs.title ==   i['title'] )

            if not query.get():
                db = dbsongs()
                db.title = i['title']
                db.creator=i['creator']
                db.location =i['location']
                db.lyric= i['lyric']
                db.put()


        self.response.out.write(json.dumps({"data":listlink}))

def main():
    application = webapp.WSGIApplication([('/', MainHandler),('/getlink', GetLinkHandler),('/getlinkjson', JsonHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
