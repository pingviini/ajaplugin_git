import unittest
from ajaplugin_git.git import Git
from aja.vcs.base import VcsBase



class GitPluginTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_meta(self):
        instance = Git()
        self.assertTrue(isinstance(instance, VcsBase))
