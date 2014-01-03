import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

setup(name='ajaplugin_git',
      version='0.1.0',
      description='',
      long_description="%s\n%s" % (README, CHANGES),
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
      ],
      author='Jukka Ojaniemi',
      author_email='jukka.ojaniemi@gmail.com',
      url='https://github.com/pingviini/ajaplugin_git',
      keywords='deploy buildout',
      package_dir={"": "src"},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'aja',
          'path.py',
      ],
      test_suite='ajaplugin_git.tests',
      entry_points={
          'aja.plugins.vcs': 'git = ajaplugin_git.git:Git',
      },
      )
