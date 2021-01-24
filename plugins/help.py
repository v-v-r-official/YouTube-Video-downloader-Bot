from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"1. Send youtube video URL (Link|New Name with Extension).\n2. Send Custom Thumbnail (Optional).\n3. Select the button.\nSVideo - Give File as video with Screenshots\nDFile  - Give File with Screenshots\nVideo  - Give File as video without Screenshots\nDFile  - Give File without Screenshots"
    await message.reply_text(helptxt)
