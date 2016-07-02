try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Testing a Game',
    'author': 'canesco',
    'url': 'url to get it at',
    'download_url': 'where to download it',
    'author_email': 'hello@kooyami.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
