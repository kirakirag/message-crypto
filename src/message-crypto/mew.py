from telethon import TelegramClient, events

# Remember to use your own values from my.telegram.org!
api_id = 2291221
api_hash = 'f788a63b55201ecf2856e33922e777d1'
client = TelegramClient('anon', api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()
    print(me.id)

    async for dialog in client.iter_dialogs():
        print(dialog.name, dialog.id)

    dialog_num = int(input('Введите ID чата '))

    async for message in client.iter_messages(dialog_num):
        sender = await message.get_sender()
        print(sender.username, message.date, message.text)

    @client.on(events.NewMessage(pattern='(?i)hello.+'))
    async def handler(event):
        # Respond whenever someone says "Hello" and something else
        await event.reply('Hey!')

    # You can send messages to yourself...
    await client.send_message('me', 'hello.')

with client:
    client.loop.run_until_complete(main())