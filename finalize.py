import pkg_resources
from subprocess import call

HELPER_PATH = pkg_resources.resource_filename('BSTSB','BSTSB_bash_helper.py')
BASH_PATH = pkg_resources.resource_filename('BSTSB','')

command = 'echo \'export BSTSB_BASH_HELPER=' + HELPER_PATH + '\' >> ~/.bashrc'
call(command,shell=True)
command = 'echo \'export PATH="' + BASH_PATH + ':$PATH"' + '\' >> ~/.bashrc'
call(command,shell=True)
command = 'chmod +x ' + BASH_PATH + '/bstsb'
call(command,shell=True)