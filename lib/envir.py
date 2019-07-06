#!/usr/bin/env python3
import os
import json
import hashlib
import datetime


class Envir:
    def __init__(self):
        envir_hash = 'LAST_{}'.format(datetime.datetime.now())

        os.environ['LAST_ENVIR'] = hashlib.sha256(envir_hash.encode('utf8')).hexdigest()

        # Define default values for the environment variables.
        os.environ['LAST_USER'] = 'user'
        os.environ['LAST_PASSWD'] = 'Ch@ngeMe1984'
        os.environ['LAST_ROOT'] = '/opt/LAST/'
        os.environ['LAST_DEBUG'] = 'False'
        os.environ['LAST_EXEC'] = '/opt/LAST/exec'

        try:
            if os.path.isfile('conf/envir.cfg'):
                self.config = json.loads(open('conf/envir.cfg', 'r').read())
                for key in self.config:
                    os.environ[key] = self.config[key]

        except json.JSONDecodeError as e:
            # log.warn(e)
            pass
