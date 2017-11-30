import pkg_resources
from subprocess import call

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

configure = input('Configure slack account now? [y/n] ')

if configure == 'y':
    USERNAME = input('Enter slack username: ')
    API_TOKEN = input('Enter slackbot API token: ')

    command = 'echo \'export SLACK_USERNAME=' + USERNAME + '\' >> ~/.bashrc'
    call(command,shell=True)
    command = 'echo \'export SLACK_BOT_TOKEN=' + API_TOKEN + '\' >> ~/.bashrc'
    call(command,shell=True)

source = input('Source ~/.bashrc from ~/.bash_profile?(MacOS) [y/n] ')

if source == 'y':
    SOURCE_STRING = ('if [ -f ~/.bashrc ]; then\n'
                     '    source ~/.bashrc\n'
                     'fi')

    command = 'echo \'export SLACK_USERNAME=' + SOURCE_STRING +\
              '\' >> ~/.bash_profile'
    call(command,shell=True)