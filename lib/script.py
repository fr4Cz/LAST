#!/usr/bin/env python3
import os
from lib import envir
import subprocess


class Script:
    def __init__(self):
        if 'LAST_ENVIR' not in os.environ:
            envir.Envir()

        self.base_path = os.environ['LAST_EXEC']

    def run(self, name, when='conf'):
        if when == 'config':
            when = 'conf'

        try:
            session = subprocess.Popen(['{}/{}/{}'.format(self.base_path, when, name)],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            stdout, stderr = session.communicate()
            if stderr:
                # log.err('Script {} ended with exception: {}'.format(name, stderr))
                print('Script {} ended with exception: {}'.format(name, stderr))
        except FileNotFoundError as e:
            # log.err(e)
            pass

    def run_final(self):
        scripts = os.listdir('{}/final/'.format(self.base_path))

        for s in scripts:
            try:
                self.run(s, when='final')
            except Exception as e:
                # log.err(e)
                pass

    def run_initial(self):
        scripts = os.listdir('{}/initial/'.format(self.base_path))

        for s in scripts:
            try:
                self.run(s, when='initial')
            except Exception as e:
                # log.err(e)
                pass
