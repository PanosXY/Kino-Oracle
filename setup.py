from setuptools import setup

PKG_NAME = 'kino-oracle'
PKG_VER = '1.0.0'

scripts = [
        'kino.py'
]

setup(
    name = PKG_NAME,
    version = PKG_VER,
    description = 'Kino number generator',
    author = 'Panagiotis Skiadas',
    author_email = 'panoskiadas@gmail.com',
    license = 'GPLv3 or later',
    scripts = scripts,
    zip_safe = False
)
