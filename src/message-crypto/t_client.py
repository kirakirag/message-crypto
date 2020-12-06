from telethon import TelegramClient, events, sync


api_id = 2291221
api_hash = 'f788a63b55201ecf2856e33922e777d1'


class Session:

    def __init__(self):
        """
        Initialization of a new session.
        """
        self.client = TelegramClient('user', api_id, api_hash)

    def start_session(self):
        """
        Start new session.
        """
        self.client.start()
        pass

    def get_fingerprint(self):
        """
        Get fingerprint for user.
        """
        return self.client.get_me().id

    def get_dialogs(self):
        """
        Get user's dialogs.
        """
        return self.client.get_dialogs()

    def stop_session(self):
        """
        Stop this session.
        """
        self.client.disconnect()

    def dialogs_for_print(self):
        dialog_list = ['{}    {}'.format(dialog[0], dialog[1].name) for dialog in enumerate(self.get_dialogs())]
        return dialog_list

    def chat_for_print(self):
        chat_number = int(input('Number of the chat you want to open '))
        message_list = []
        for message in self.client.get_messages(self.get_dialogs()[chat_number].entity, 20):
            message_list.append('From {} at {}: {}'.format(message.get_sender().username,
                                                           message.date, message.message))
        return message_list


c = Session()
c.start_session()
print(*c.dialogs_for_print(), sep='\n')
print(*c.chat_for_print(), sep='\n')
c.stop_session()