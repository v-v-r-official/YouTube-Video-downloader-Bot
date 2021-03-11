from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⭕️CHANNEL⭕️", url="https://t.me/VKPROJECTS"),
        [InlineKeyboardButton(
            "⭕️GROUP⭕️", url="https://t.me/VKP_BOTS), InlineKeyboardButton(text="♐️SHARE♐️", url="tg://msg?text=Hai%20Friend+❤️,+Today%20i+just+found+out+an+intresting+and+Powerful+**YouTube+Bot**+for+Free🥰.+**Bot+Link**+:+@YouTubeVKbot+🔥")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n**I'm A POWERFULL YOUTUBE DOWNLOADER Bot💯\nPlease send me any YOUTUBE link,\nClick /help for more detailS..\nYou must subscribe our channel in order to use me😇**"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
