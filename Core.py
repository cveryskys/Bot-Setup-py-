# i use this for like all my discords bots- quick + easy setup , read the README to understand further

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKE')
print(f"Token: {TOKEN}") 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'started bot ; {bot.user}!')
    try:
        synced = await bot.tree.sync()
        print(f'sycned {len(synced)} commands')
    except Exception as e:
        print(f'error syncing commands: {e}')

async def load_commands():
    for filename in os.listdir('./Commands'):
        if filename.endswith('.py') and filename != '__init__.py':
            await bot.load_extension(f'Commands.{filename[:-3]}')


async def main():
    await load_commands()
    await bot.start(TOKEN)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
