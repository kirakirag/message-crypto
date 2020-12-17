import asyncio

from telethon import TelegramClient, events

api_id = 2291221
api_hash = 'f788a63b55201ecf2856e33922e777d1'
client = TelegramClient('anon', api_id, api_hash)
dialog_num = 0


@client.on(events.NewMessage())
async def my_event_handler(event):
    chat = await event.get_chat()
    global dialog_num
    if chat.id == dialog_num:
        if event.text == '/encrypt':
            await client.delete_messages(chat.id, [event.id])
            message_to_send = input()
            await client.send_message(chat, message_to_send)
        else:
            sender = await event.get_sender()
            print(sender.username, event.date, event.text)


async def main():

    me = await client.get_me()
    print(me.id)

    async for dialog in client.iter_dialogs():
        print(dialog.name, dialog.id)

    global dialog_num
    dialog_num = int(input('Введите ID чата '))

    async for message in client.iter_messages(dialog_num):
        sender = await message.get_sender()
        print(sender.username, message.date, message.text)


with client:
    client.loop.run_until_complete(main())
    print(dialog_num)
    client.start()
    client.run_until_disconnected()