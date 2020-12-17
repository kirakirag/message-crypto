import asyncio

from telethon import TelegramClient, events

from pki import Encrypt, Decrypt, KeyManager

# Remember to use your own values from my.telegram.org!
api_id = 'some_api_id'
api_hash = 'some_api_hash'
client = TelegramClient('anon', api_id, api_hash)
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
            if recipient:
                await client.delete_messages(chat.id, [event.id])
                message_to_send = encrypt_string(recipient, input('Enter message: '))
                await client.send_message(chat, message_to_send)
        else:
            print(sender.username, event.date, event.text)


async def main():

    me = await client.get_me()
    global me_id
    me_id = me.id

    async for dialog in client.iter_dialogs():
        print(dialog.name, dialog.id)

    global dialog_num
    dialog_num = int(input('Введите ID чата '))

    async for message in client.iter_messages(dialog_num):
        sender = await message.get_sender()
        print(sender.username, message.date, message.text)


with client:
    client.loop.run_until_complete(main())
    client.start()
    client.run_until_disconnected()