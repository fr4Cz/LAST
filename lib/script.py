#!/usr/bin/env python3
import os
from lib import envir
import subprocess
#   Todo; Implement logging
#   Scripts seems to run OK. However, there is no logging in place.


class Script:
    def __init__(self):
        if 'LAST_ENVIR' not in os.environ:
            envir.Envir()

        self.base_path = os.environ['LAST_EXEC']

    def run(self, name, when='conf'):
        if when == 'config':
            when = 'conf'
        try:
            script_path = '{}/{}/{}'.format(self.base_path, when, name)

            # Ensure script exists and is executable
            if os.path.isfile(script_path):
                if not os.access(script_path, os.X_OK):
                    os.chmod(script_path, 0o755)

            session = subprocess.Popen([script_path],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            stdout, stderr = session.communicate()

            if stdout:
                print(stdout.decode('utf-8'))
            if stderr:
                # log.err('Script {} ended with exception: {}'.format(name, stderr))
                print('Script {} ended with exception: {}'.format(name, stderr.decode('utf-8')))
        except FileNotFoundError as e:
            # log.err(e)
            # print(e)
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
