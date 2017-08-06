from setuptools import setup

setup(
    name='Unicorn Remote',
    author='Nathaniel Baer',
    author_email='njbbaer@gmail.com',
    url='https://github.com/njbbaer/unicorn-remote',
    install_requires = [
        'Flask',
        'flask_restful',
        'unicornhat',
        'pyfiglet'
    ]
)
