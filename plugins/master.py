from pyrogram import Client as bot, filters
from config import Config
import shutil
import os
from master import masterdl

@bot.on_message(filters.command("drm"))
async def account_login(bot, m):
    try:
        Credit = Config.CREDIT
        editable = await m.reply_text('__Send 🗂️Master TXT🗂️ file for download__')
        input = await bot.listen(chat_id=m.chat.id)
        path = f"./downloads/{m.chat.id}"
        temp_dir = "./temp"
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)
        links, file_name = await masterdl.process_text_file_or_input(input)
        await editable.edit(f"Total links🔗 found are __{len(links)}__\n\nSend From where you want to download initial is __1__")
        input0=await bot.listen(chat_id=m.chat.id)
        raw_text = input0.text
        await input0.delete(True)

        await editable.edit("__Enter Batch Name or send 1 for grabbing from text filename.__")
        input1=await bot.listen(chat_id=m.chat.id)
        raw_text0 = input1.text
        await input1.delete(True)
        if raw_text0 == '1':
            b_name = file_name
        else:
            b_name = raw_text0

        await editable.edit("__Enter resolution__\n\nEg - `360` or `480` or `720`")
        input2=await bot.listen(chat_id=m.chat.id)
        raw_text2 = input2.text
        await input2.delete(True)

        await editable.edit(f"__Enter Your Name\n\nSend 1 for `{Credit}`")
        input3=await bot.listen(chat_id=m.chat.id)
        raw_text3 = input3.text
        await input3.delete(True)
        if raw_text3 == '1':
            MR = Credit
        else:
            MR = raw_text3

        await editable.edit("Send PW Working Token\nFor default send 1")
        input4 = await bot.listen(chat_id=m.chat.id)
        token = input4.text
        await input4.delete(True)
        await editable.edit("Now send the __Thumb URL__\n\nor Send `no`")
        input6=await bot.listen(chat_id=m.chat.id)
        thumb = input6.text
        await input6.delete(True)
        
        await editable.edit("__Please Provide Channel id to Upload video otherwise `/d` __\n\n__And make me admin in this channel then i can able to Upload otherwise i can't__")
        input7=await bot.listen(chat_id=m.chat.id)
        if "/d" in input7.text:
            channel_id = m.chat.id
        else:
            channel_id = input7.text

        await input7.delete()
        try:
            await bot.send_message(chat_id=channel_id, text=f'🎯**Target Batch - {b_name}**')
        except Exception as e:
            await m.reply_text(f"**Please remake a admin in channel..**\n\n**Bot Made By** 🔰『{Credit}🔰")
            channel_id=m.chat.id
        await editable.delete()
        await masterdl.process_links(links, raw_text, raw_text2, token, b_name, MR, channel_id, bot, m, path, thumb, Credit)
    except Exception as e:
        await m.reply_text(f"**⚠️Downloading Failed⚠️**\n\n**Fail Reason »** {e}\n\n**╰────⌈✨❤️ 『{Credit}』 ❤️✨**⌋────╯")
        return
    
