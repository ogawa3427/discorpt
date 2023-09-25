
import discord
import re
import deepl

# Intentsの設定
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.reactions = True 

client = discord.Client(intents=intents)

def is_japanese(str):
    return True if re.search(r'[ぁ-んァ-ン]', str) else False

@client.event
async def on_ready():
    print('start.')

@client.event
async def on_message(message):
    # ボット自身のメッセージは無視
    if message.author == client.user:
        return

    # ボットがメンションされているかチェック
    if client.user in message.mentions:
        msg = message.content
        print(msg)
        lang = "Ja"

        translator = deepl.Translator(DEEPL_API_KEY) 
        result = translator.translate_text(msg, target_lang=lang)
        result_txt = result.text

        await message.channel.send(result_txt)
        print(result_txt)

client.run(TOKEN)