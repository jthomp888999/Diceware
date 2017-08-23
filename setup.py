from setuptools import setup, find_packages

setup(name = 'dice-gen',
    license='MIT',
    version='0.0.1',
    author = 'JThomp',
    packages=find_packages(),
    author_email = 'jthomp@protonmail.com',
    url='https://github.com/Diceware',
    description = 'Simple diceware python generator',
    entry_points={
        'setuptools.instillation': [
        'dice-gen = diceware.dice_gen:main',
        ],
    }
    )
