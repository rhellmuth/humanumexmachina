#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rudolf Hellmuth'
SITENAME = u'Humanum ex Machina'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Dublin'
DEFAULT_LANG = u'pt'
LANG = u'pt_BR.UTF-8'
DEFAULT_PAGINATION = 10

ARTICLE_URL = 'posts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'

# Title menu options
# MENUITEMS = [('Archives', '/archives.html'),
# 			]

STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.ico']
CODE_DIR = 'downloads/codes'
NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plugins
THEME = "./notmyidea-rh"
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['summary', 
		   'liquid_tags.img',
		   'liquid_tags.video',
           'liquid_tags.include_code', 
           'liquid_tags.notebook',
           'liquid_tags.literal',
           'sitemap',
           'latex',
           ]
SUMMARY_END_MARKER = "<!-- more -->"
FAVICON = 'favicon.ico'
SITEMAP = {'format': 'xml',
    	   'priorities': {'articles': 0.5, 'indexes': 0.5, 'pages': 0.5},
    	   'changefreqs': {'articles': 'monthly',
    	   				   'indexes': 'daily', 
    	   				   'pages': 'monthly'}
		  }


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/rhellmuth'),
		 )
# GITHUB_URL = 'http://github.com/rhellmuth/'
GITHUB_USER = 'rhellmuth'
GITHUB_SHOW_USER_LINK = False



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'


# Search
SEARCH_BOX = True
