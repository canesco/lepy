try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'canesco',
    'url': 'url to get it at',
    'download_url': 'where to download it',
    'author_email': 'hello@kooyami.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'], # filename without .py
    'scripts': [],
    'name': 'projectname' # package name
}

setup(**config)
