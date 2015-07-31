# -*- coding:utf-8 -*-
import requests
from lxml import sax, etree
import xmltodict

URL = "http://thegamesdb.net/api/GetGame.php?id={}"

# Alias function to xmltodict
xml_to_dict = lambda elem: xmltodict.parse(elem, process_namespaces=True)


class GameDb(object):

    def __init__(self, *args, **kwargs):
        self.get_game_url = "http://thegamesdb.net/api/GetGame.php?id={}"
        self.search_url = "http://thegamesdb.net/api/GetGame.php?id={}"
        self.platform_list = \
            "http://wiki.thegamesdb.net/index.php/GetPlatformsList"

    def get_game_info(self, id):
        resp = requests.get(self.get_game_url.format(id))
        xml = etree.fromstring(resp.content)
        url_img = xml.find("baseImgUrl").text
        game_tag = xml.find("Game")
        game_dict = xml_to_dict(etree.tostring(game_tag))
        info_dict = game_dict.get("Game")
        info_dict["url_img"] = url_img
        return dict(info_dict)
