#!/usr/bin/env python3
import os
import json
from git import Repo, GitError
from lib.envir import Envir
from lib.script import Script


class GitFetch:
    def __init__(self):
        if 'LAST_ENVIR' not in os.environ:
            Envir()

        self.script = Script()

        try:
            self.config = json.loads(open('conf/git.cfg', 'r').read())
        except json.JSONDecodeError as e:
            # log.warn(e)
            pass

        # Define supported git repos, additional repos can be added through self.add_private('repo-name')
        self.git_versions = ['github', 'gitlab']

    def install(self):
        for git in self.git_versions:
            if git in self.config:
                # Username and password only used for private packages.
                username = ''
                password = ''
                ssh_key = ''

                if 'ssh_key' in self.config[git]:
                    ssh_key = self.config[git]['ssh_key']
                else:
                    if len(self.config[git]['username']) > 0:
                        username = self.config[git]['username']

                    if len(self.config[git]['password']) > 0:
                        password = self.config[git]['password']

                for pkg in self.config[git]['packages']:
                    try:
                        repo = Repo.clone_from(pkg['url'], '{}{}/{}'.format(os.environ['LAST_ROOT'], pkg['type'], pkg['name']))
                    except GitError as e:
                        # log.warn(e)
                        pass

                    if 'config' in pkg:
                        # Todo; run script in pkg['config']
                        config_path = '{}/conf/{}'.format(os.environ['LAST_EXEC'], pkg['config'])
                        self.script.run(pkg['config'], when='conf')
            else:
                # log.warn('No such config: {}'.format(git))
                pass

    def add_private(self, name):
        self.git_versions.append(name)
