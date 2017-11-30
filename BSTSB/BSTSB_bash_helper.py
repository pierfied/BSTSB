import os
import sys
from BSTSB import BSTSB
from subprocess import call
import pkg_resources

def nice_try_protocol():
    print('Nice try boi!')
    bot = BSTSB()
    NTP_PATH = pkg_resources.resource_filename('BSTSB',
                                               'nice_try_protocol.jpg')
    bot.send_file(NTP_PATH)
    exit(1)

if __name__=="__main__":
    if len(sys.argv) < 2:
        nice_try_protocol()

    command = sys.argv[1:]

    background = False
    if sys.argv[1] == '-bg':
        background = True
        command = sys.argv[2:]

    if background and len(sys.argv) < 3:
        nice_try_protocol()

    command = ' '.join(command)

    if background:
        pid = os.fork()
        if pid > 0:
            exit(0)
        os.setsid()

        with open('out.txt','w') as outfile:
            ret_val = call(command,shell=True,stdout=outfile,stderr=outfile)
    else:
        ret_val = call(command,shell=True)

    bot = BSTSB()
    if ret_val != 0:
        bot.failed()
    else:
        bot.finished()

    exit(ret_val)