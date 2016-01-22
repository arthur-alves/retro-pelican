#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Arthur Alves'
SITENAME = u'Fullstack Arthur'
SITEURL = u'http://localhost:8000'
SITENAME = u"Arthur Alves Devlog"
SITETITLE = AUTHOR
SITESUBTITLE = u'Fullstack Developer - Pythonista'
SITEDESCRIPTION = u'{} devlog'.format(AUTHOR)

PATH = 'content'
THEME = 'Flex'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True

# Blogroll
# LINKS = (('Fullstack Arthur', 'arthur-alves.github.io'),)

# Social widget
SOCIAL = (('github', 'http://github.com/arthur-alves'),
          ('twitter', 'http://twitter.com/arthur_4lves'),
          ('linkedin', 'https://www.linkedin.com/in/arthur4lves'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
