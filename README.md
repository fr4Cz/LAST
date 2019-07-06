# Linux After Setup Tool (LAST)
LAST is a GNU/Linux configuration tool, designed to ease the personalisation of your distribution to suite all your 
personal configuration needs. It is a derivative of the [Post Kali Installer][1] which was built for easing the personal 
configuration of [Kali Linux][2]. The tool is designed mainly for Debian based distributions but can easily be tweaked
to suite most GNU/Linux distributions and possibly even BSD or macOS.


## Package managers


## Web fetch
Packages/software which is not available through a package manager or Git can be fetched directly from the web with
web fetch. All packages are fetched and stored according through their configuration with:
```
w = webfetch.WebFetch()
w.get()
```

### Adding fetchable content
Packages are added to conf/wget.cfg with the following syntax:
```
[
    {
        "name": "FooBar",
        "url": "https://foo.bar.com/baz.pl",
        "destination": "tools/FooBar"
    },
]
```

 
## Git repositories
By default LAST will support links from GitHub and GitLab, but can fetch from any git repo of choice.
To add a git repo to fetch from remember to add it in your install.py by using the git.add_private method as such:
```
g = git.GitFetch()

g.add_private('gitFoo')
g.add_private('gitBar')

g.install()
```
The example above will make LAST look for the config block of gitFoo and gitBar in packages/git.cfg.
### Adding repositories
To add repositories in the packages/git.cfg simply append a block containing the following configuration 
(NOTE! User names and passwords are only required if the repository it self requires it):
```
"gitFoo": {
        "username": "John",
        "password": "Doe123!",
        "packages": [
            {
                "name": "dummy-pkg",
                "url": "https://gitfoo.xyz/SOMEUSER/dummy-pkg.git",
                "config": "dummy_config.sh",
                "type": "tools"
            }
        ]
    }
```
Remember to always use JSON formatting in the configuration files for less surprises!


## Scripts
Custom scripts for running tasks not integrated into LAST can be executed through regular shell scripts. 
To ease any conflict of interest there are multiple environment variables which can be used to better integrate these 
scripts with LAST. For more information on environment variables see the section for environment variables.

### Timing
Scripts are run in a top to bottom fashion so any script placed first in the list will be executed first.
In addition to this there are three separate times a script can be run `initial`,`final` and `conf`.

#### Initial
These scripts will run directly after any package manager and can be used for any task which is crucial for any of 
the following processes, this could be dependencies or system changes which needs to be preformed first.  

#### Final
These scripts will run in the final stage of LAST and are suited for any task which must be done after all installations 
have finished. Commonly used for last minute configurations such as wallpapers or theme settings.

#### Conf
Conf scripts are reserved for git installations, these are used for automating the installation of any git packages
fetched if needed.


## Environment variables
LAST has multiple environment variables set by default and it is easy to extend the existing list.
The following variables are available by default (consult lib/envir.py for further details):
* LAST_USER
* LAST_PASSWD
* LAST_ROOT
* LAST_DEBUG
* LAST_EXEC

### Overriding environment variables
To override a default environment variable simply add it to a named list in conf/envir.cfg
```
{
    "LAST_ROOT": "/home/foo/bar"
}
``` 

### Extending LAST environment variables
It is easy to add custom variables to LAST, and is simply done by adding a json named list to conf/envir.cfg
```
{
    ...
    "CUSTOM_VARIABLE": "Foo"
}
```
Which will then be available for use in scripts following standard bash syntax as such: `${CUSTOM_VARUABLE}`


[1]: https://github.com/MOCHZ/PostKaliInstaller
[2]: https://kali.org/