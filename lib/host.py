#!/usr/bin/env python3
import os
import sys
import json


class Os:
    def __init__(self):
        supported = ['darwin', 'linux']

        if sys.platform not in supported:
            raise OSError('The Operating System is not supported')

        try:
            if os.path.isfile('conf/packages.cfg'):
                self.config = json.loads(open('conf/packages.cfg', 'r').read())
        except json.JSONDecodeError as e:
            # log.warn(e)
            pass

    def install(self):
        print(self.config)
        """
        Todo; Add support for installing dpkg packages through apt,
        may want to add support for dnf and packman as well!
        """

    def _apt(self, pkg):
        pass
