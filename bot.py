import discord

from discord_gpt.chat_completion import GptModel
from discord_gpt.client import OpenAIClient
from settings import settings

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        generated_text = OpenAIClient.complete(
            prompt='How old is Putin?',
            model=GptModel.GPT_3_5_TURBO_0301,
        )
        await message.channel.send('Hello!')

client.run(settings.TOKEN)
