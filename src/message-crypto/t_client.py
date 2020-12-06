from telethon import TelegramClient, events, sync


api_id = 2291221
api_hash = 'f788a63b55201ecf2856e33922e777d1'


with TelegramClient('user', api_id, api_hash) as client:
    me = client.get_me()
    fingerprint = me.id
    dialogs = client.get_dialogs()
    for dialog in enumerate(dialogs):
        print(dialog[0], dialog[1].name)
    chat_number = int(input('Number of the chat you want to open '))
    for message in client.get_messages(dialogs[chat_number].entity, 20):
        print('From {} at {}: {}'.format(message.get_sender().username, message.date, message.message))