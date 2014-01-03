import logging
import subprocess
import shlex

from path import path
from aja.vcs.base import VcsBase


class Git(VcsBase):
    """Aja Git support."""

    def pull(self, repository_uri):
        logging.info("Cloning repository {uri}.".format(uri=repository_uri))
        cmd = "git clone {uri}".format(uri=repository_uri)
        self.run(cmd)

    def update(self):
        logging.info("Updating repository {path}".format(path=repository))
        cmd = "git pull"
        self.run(cmd)

    def run(self, cmd):
        """Execute generated command in given working dir."""
        with path(self.working_dir):
            try:
                subprocess.check_call(cmd)
            except subprocess.CalledProcessError as e:
                logging.error(str(e))
