from distutils.core import setup
import py2exe

setup(
    name = 'Diceware Generator',
    version = '0.0.1',
    author = 'John Thompson',
    author_email = 'jthomp@protonmail.com',
    description = 'Simple diceware python generator',
    install_requires = ['pyperclip'],
    options = {'py2exe': {'bundle_files': 1,'compressed': True}},
    console = [{'script': "dice.py"}],
    zipfile = None,
)