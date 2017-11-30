from setuptools import setup
from subprocess import call
import os,sys,site

def binaries_directory():
    """Return the installation directory, or None"""
    if '--user' in sys.argv:
        paths = (site.getusersitepackages(),)
    else:
        py_version = '%s.%s' % (sys.version_info[0], sys.version_info[1])
        paths = (s % (py_version) for s in (
            sys.prefix + '/lib/python%s/dist-packages/',
            sys.prefix + '/lib/python%s/site-packages/',
            sys.prefix + '/local/lib/python%s/dist-packages/',
            sys.prefix + '/local/lib/python%s/site-packages/',
            '/Library/Python/%s/site-packages/',
        ))

    for path in paths:
        if os.path.exists(path):
            return path
    print('no installation path found', file=sys.stderr)
    return None

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

call('python finalize.py',shell=True)

#import BSTSB

# BASH_PATH = binaries_directory() + 'BSTSB'
# HELPER_PATH = binaries_directory() + 'BSTSB/BSTSB_bash_helper.py'
#
# command = 'echo \'export BSTSB_BASH_HELPER=' + HELPER_PATH + '\' >> ~/.bashrc'
# call(command,shell=True)
# command = 'echo \'export PATH="' + BASH_PATH + ':$PATH"' + '\' >> ~/.bashrc'
# call(command,shell=True)