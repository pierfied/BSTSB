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

call('rm -rf BSTSB',shell=True)

HELPER_PATH = pkg_resources.resource_filename('BSTSB','BSTSB_bash_helper.py')
BASH_PATH = pkg_resources.resource_filename('BSTSB','')

command = 'echo \'export BSTSB_BASH_HELPER=' + HELPER_PATH + '\' >> ~/.bashrc'
call(command,shell=True)
command = 'echo \'export PATH="' + BASH_PATH + ':$PATH"' + '\' >> ~/.bashrc'
call(command,shell=True)
command = 'chmod +x ' + BASH_PATH + '/bstsb'
call(command,shell=True)

try: input = raw_input
except NameError: pass

configure = input('Configure slack account now? (y/n) ')

if configure == 'y':
    USERNAME = input('Enter slack username: ')
    API_TOKEN = input('Enter slackbot API token: ')

    command = 'echo \'export SLACK_USERNAME=' + USERNAME + '\' >> ~/.bashrc'
    call(command,shell=True)
    command = 'echo \'export SLACK_BOT_TOKEN=' + API_TOKEN + '\' >> ~/.bashrc'
    call(command,shell=True)