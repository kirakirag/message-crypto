import asyncio

from telethon import TelegramClient, events

from pki import Encrypt, Decrypt, KeyManager

# Load Telegram credentials from file
with open('credentials', 'r') as f:
    data = f.readline().split(';')
    api_id = int(data[0])
    api_hash = data[1]


client = TelegramClient('kira', api_id, api_hash)
dialog_num = 0
me_id = 0

encrypt = Encrypt.Encrypt()
encrypt_string = encrypt.encrypt_string
decrypt = Decrypt.Decrypt(input('Enter passphrase for your private key: '))
decrypt_string = decrypt.decrypt_string
keys = KeyManager.KeyManager()


@client.on(events.NewMessage())
async def my_event_handler(event):
    chat = await event.get_chat()
    sender = await event.get_sender()
    global dialog_num
    if chat.id == dialog_num:
        if event.text == '/encrypt' and sender.id == me_id:
            recipient = keys.get_key_by_id(chat.id)
            print('Chat id = ', chat.id)
            if recipient:
                await client.delete_messages(chat.id, [event.id])
                message_to_send = encrypt_string(recipient, input('Enter message: '))
                await client.send_message(chat, message_to_send)
        else:
            if 'BEGIN PGP MESSAGE' in event.text:
                data = decrypt_string(event.text)
                if data:
                    print(sender.username, event.date, data)
                else:
                    print('\n\n\n===We do not have a private key for this message, skipping.===\n\n\n')
            else:
                print(sender.username, event.date, event.text)


async def main():

    me = await client.get_me()
    global me_id
    me_id = me.id
    dialogs = []

    async for dialog in client.iter_dialogs():
        dialogs.append(dialog.id)
        print(dialog.name, dialog.id)
        print('\n--------------')

    global dialog_num
    #dialog_num = int(input('Enter chat id: \n'))
    while dialog_num not in dialogs:
        dialog_num = int(input('Enter chat id: \n'))

    async for message in client.iter_messages(dialog_num):
        sender = await message.get_sender()
        if 'BEGIN PGP MESSAGE' in message.text:
            data = decrypt_string(message.text)
            if data:
                print(sender.username, message.date, data)
            else:
                print('\n\n\n===We do not have a private key for this message, skipping.===\n\n\n')
        else:
            print(sender.username, message.date, message.text)
            print('----------------')


with client:
    client.loop.run_until_complete(main())
    client.start()
    client.run_until_disconnected()