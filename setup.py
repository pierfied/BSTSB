from setuptools import setup
from subprocess import call
import pkg_resources
import os,sys,site

setup(name='BSTSB',
      version='0.1',
      description='Bot Script the Script Bot',
      url='http://github.com/pierfied/BSTSB',
      author='Pier Fiedorowicz',
      author_email='pierfied@email.arizona.edu',
      license='MIT',
      packages=['BSTSB'],
      zip_safe=False,
      data_files=[('BSTSB',['BSTSB/bsod.png','BSTSB/nice_try_protocol.jpg',
                            'BSTSB/BSTSB_bash_helper.py','BSTSB/bstsb'])])

call('python finalize.py',shell=True)