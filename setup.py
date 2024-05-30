from glob import glob
from os.path import basename, splitext
from setuptools import setup
from setuptools.command.install import install
import subprocess

install_requires = [
    'quart',
    'google-auth',
    'google-auth-oauthlib',
    'google-auth-httplib2',
    'google-api-python-client',
    'python-dotenv'
]

setup(
    name='calendar',  
    version='1.0.0', 
    py_modules=[splitext(basename(path))[0] for path in glob('*.py')],  
    install_requires=install_requires,
    author='jii1n',
    author_email='yj5596901@gmail.com',
    description='Desc'
)
