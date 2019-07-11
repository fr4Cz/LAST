#!/usr/bin/env python3
import os
import wget
import json


class WebFetch:
    def __init__(self):
        if os.path.isfile('conf/wget.cfg'):
            try:
                self.config = json.loads(open('conf/wget.cfg', 'r').read())
            except json.JSONDecodeError as e:
                # log.warn(e)
                print('JSON Error: {}'.format(e))

    def get(self):
        try:
            for pkg in self.config:
                try:
                    print('Downloading: {}'.format(pkg['name']))
                    if not os.path.isdir(pkg['destination']):
                        try:
                            os.makedirs(pkg['destination'])
                        except OSError as e:
                            # log.err(e)
                            print(e)
                            pass
                    wget.download(pkg['url'], out=pkg['destination'])
                except Exception as e:
                    # log.warn(e)
                    print(e)
                    pass
        except Exception as e:
            # log.err(e)
            print(e)
            pass
