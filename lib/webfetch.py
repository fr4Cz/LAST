#!/usr/bin/env python3
import os
import wget
import json


class WebFetch():
    def __init__(self):
        try:
            if os.path.isfile('conf/wget.cfg'):
                self.config = json.loads(open('conf/wget.cfg', 'r').read())
        except json.JSONDecodeError as e:
            # log.warn(e)
            pass

    def get(self):
        for pkg in self.config:
            # Todo; implement wget
            pass
