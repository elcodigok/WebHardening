#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class Plugins():

    def __init__(self):
        self._STAGE_NAMES = [
            'blogs', 
            'ecommerce', 
            'elearning', 
            'forums', 
            'groupware', 
            'imageGalleries', 
            'portals', 
            'wiki',
        ]

    def get_stage_name(self, stage_number):
        if stage_number >= 0:
            try:
                return self._STAGE_NAMES[stage_number]
            except IndexError:
                pass

    def get_list_plugins(self):
        return self._STAGE_NAMES

    def get_item_plugis(self, item):
        return self._STAGE_NAMES[item]