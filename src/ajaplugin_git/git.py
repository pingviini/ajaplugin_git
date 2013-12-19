import logging
import subprocess
import shlex

from path import path
from aja.vcs.base import VcsBase


class Git(VcsBase):
    """Aja git support."""

    def pull(self, repository_uri, destination, **kwargs):
        logging.info("Cloning repository {uri} to {path}".format(
            uri=repository_uri, path=destination))
        with path(destination):
            cmd = "git clone {uri}".format(uri=repository_uri)
            subprocess.check_call(shlex.split(cmd))

    def update(self, repository):
        logging.info("Updating repository {path}".format(path=repository))
        with path(repository):
            cmd = "git pull"
            subprocess.check_call(shlex.split(cmd))
