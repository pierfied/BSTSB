import os
from slackclient import SlackClient
import pkg_resources

class BSTSB:
    def __init__(self):
        self.USERNAME = os.environ.get('SLACK_USERNAME')
        self.slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
        self.USER_ID = None

        api_call = self.slack_client.api_call("users.list")
        if api_call.get('ok'):
            # retrieve all users so we can find our bot
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == self.USERNAME:
                    self.USER_ID = user.get('id')
        else:
            print("could not find user with the name " + self.USERNAME)

        self.convo = self.slack_client.api_call('conversations.open',
                                                users=self.USER_ID)
        self.DM_ID = self.convo.get('channel').get('id')

    def send_message(self,msg):
        self.slack_client.api_call('chat.postMessage',
                                   channel=self.DM_ID,
                                   text=msg)

    def send_file(self,f_name,msg=None):
        if msg is not None:
            self.slack_client.api_call('chat.postMessage',
                                       channel=self.DM_ID,
                                       text=msg)

        self.slack_client.api_call('files.upload',
                                   channels=self.DM_ID,
                                   file=open(f_name,'rb'))

    def finished(self):
        self.send_message('Yo! Your job is done')

    def failed(self):
        self.send_message('404 Windows Not Found')
        BSOD_PATH = pkg_resources.resource_filename('BSTSB','bsod.png')
        self.send_file(BSOD_PATH)
        self.send_message('Ya but seriously your code is messed up')