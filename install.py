#!/usr/bin/env python3
import os
import sys
import lib.gitfetch as gitfetch
import lib.script as script
import lib.envir as envir
import lib.host as host
import lib.webfetch as webfetch


def main():
    envir.Envir()

    g = gitfetch.GitFetch()
    s = script.Script()
    h = host.Os()
    w = webfetch.WebFetch()

    # Currently testing script functionality in git config and script.
    # Scripts are currently located under exec/conf, exec/final and exec/init
    g.install()
    # w.get()
    s.run_initial()
    s.run_final()


if __name__ == '__main__':
    if os.getuid() > 0:
        sys.exit('Installation must be run with sudo')
    else:
        main()
